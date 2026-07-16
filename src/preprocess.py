from pathlib import Path
import json
from datetime import datetime, timezone

import pandas as pd
from sklearn.model_selection import train_test_split


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
PROCESSED_DIR = DATA_DIR / "processed"

REPORTS_DIR = PROJECT_ROOT / "reports"

REPORTS_DIR.mkdir(exist_ok=True)


# ============================================================
# DATA LOADER
# ============================================================

def load_processed_artifact(file_stem):
    csv_path = PROCESSED_DIR / f"{file_stem}.csv"

    if csv_path.exists():
        return pd.read_csv(csv_path)

    raise FileNotFoundError(f"Could not find {file_stem}")


# ============================================================
# LOAD DATASETS
# ============================================================

def load_datasets():
    X_full = load_processed_artifact("X_full")
    X_early = load_processed_artifact("X_early")

    try:
        y = load_processed_artifact("y_full")
    except FileNotFoundError:
        y = load_processed_artifact("y_early")

    if isinstance(y, pd.DataFrame):
        y = y.iloc[:, 0]

    y.name = "G3"

    return X_full, X_early, y


# ============================================================
# VALIDATION
# ============================================================

def validate_datasets(X_full, X_early, y):

    assert isinstance(X_full, pd.DataFrame)
    assert isinstance(X_early, pd.DataFrame)
    assert isinstance(y, pd.Series)

    assert "G3" not in X_full.columns
    assert "G3" not in X_early.columns

    assert "G1" in X_full.columns
    assert "G2" in X_full.columns

    assert "G1" not in X_early.columns
    assert "G2" not in X_early.columns

    assert len(X_full) == len(y)
    assert len(X_early) == len(y)

    assert X_full.index.equals(y.index)
    assert X_early.index.equals(y.index)

    return True


# ============================================================
# TRAIN TEST SPLIT
# ============================================================

def create_splits(
    X_full,
    X_early,
    y,
    test_size=0.20,
    random_state=42
):

    Xtr_f, Xte_f, ytr_f, yte_f = train_test_split(
        X_full,
        y,
        test_size=test_size,
        random_state=random_state,
        shuffle=True
    )

    Xtr_e, Xte_e, ytr_e, yte_e = train_test_split(
        X_early,
        y,
        test_size=test_size,
        random_state=random_state,
        shuffle=True
    )

    return {
        "Xtr_f": Xtr_f,
        "Xte_f": Xte_f,
        "ytr_f": ytr_f,
        "yte_f": yte_f,
        "Xtr_e": Xtr_e,
        "Xte_e": Xte_e,
        "ytr_e": ytr_e,
        "yte_e": yte_e,
    }


# ============================================================
# SPLIT VALIDATION
# ============================================================

def validate_splits(splits):

    assert splits["Xtr_f"].index.equals(
        splits["Xtr_e"].index
    )

    assert splits["Xte_f"].index.equals(
        splits["Xte_e"].index
    )

    pd.testing.assert_series_equal(
        splits["ytr_f"],
        splits["ytr_e"]
    )

    pd.testing.assert_series_equal(
        splits["yte_f"],
        splits["yte_e"]
    )

    assert set(
        splits["Xtr_f"].index
    ).isdisjoint(
        splits["Xte_f"].index
    )

    return True


# ============================================================
# REPRODUCIBILITY CHECK
# ============================================================

def check_reproducibility(
    X_full,
    y,
    splits,
    test_size=0.20,
    random_state=42
):

    Xtr_r, Xte_r, ytr_r, yte_r = train_test_split(
        X_full,
        y,
        test_size=test_size,
        random_state=random_state,
        shuffle=True
    )

    pd.testing.assert_frame_equal(
        splits["Xtr_f"],
        Xtr_r
    )

    pd.testing.assert_frame_equal(
        splits["Xte_f"],
        Xte_r
    )

    pd.testing.assert_series_equal(
        splits["ytr_f"],
        ytr_r
    )

    pd.testing.assert_series_equal(
        splits["yte_f"],
        yte_r
    )

    return True


# ============================================================
# SUMMARY TABLES
# ============================================================

def create_split_summary(splits):

    return pd.DataFrame({
        "Scenario": [
            "Full",
            "Early Warning"
        ],
        "Train Rows": [
            len(splits["Xtr_f"]),
            len(splits["Xtr_e"])
        ],
        "Test Rows": [
            len(splits["Xte_f"]),
            len(splits["Xte_e"])
        ],
        "Features": [
            splits["Xtr_f"].shape[1],
            splits["Xtr_e"].shape[1]
        ]
    })


def create_validation_table(splits):

    return pd.DataFrame({
        "Check": [
            "Same train students",
            "Same test students",
            "No overlap"
        ],
        "Result": [
            splits["Xtr_f"].index.equals(
                splits["Xtr_e"].index
            ),
            splits["Xte_f"].index.equals(
                splits["Xte_e"].index
            ),
            set(
                splits["Xtr_f"].index
            ).isdisjoint(
                splits["Xte_f"].index
            )
        ]
    })

# ============================================================
# SAVE SPLITS
# ============================================================

def save_splits(splits):

    files = {
        "X_train_full": splits["Xtr_f"],
        "X_test_full": splits["Xte_f"],
        "y_train_full": splits["ytr_f"].to_frame(),
        "y_test_full": splits["yte_f"].to_frame(),

        "X_train_early": splits["Xtr_e"],
        "X_test_early": splits["Xte_e"],
        "y_train_early": splits["ytr_e"].to_frame(),
        "y_test_early": splits["yte_e"].to_frame(),
    }

    for name, df in files.items():
        csv_path = PROCESSED_DIR / f"{name}.csv"

        df.to_csv(csv_path, index=False)

    return files

# ============================================================
# MANIFEST
# ============================================================

def create_manifest(
    X_full,
    X_early,
    y,
    splits,
    summary
):

    manifest = {

        "session": 22,

        "title": "Train/Test Split",

        "created_utc":
            datetime.now(timezone.utc).isoformat(),

        "rows": len(y),

        "full_features":
            X_full.shape[1],

        "early_features":
            X_early.shape[1],

        "train_rows":
            len(splits["Xtr_f"]),

        "test_rows":
            len(splits["Xte_f"]),

        "random_state": 42,

        "test_size": 0.20,

        "same_train_students":
            splits["Xtr_f"].index.equals(
                splits["Xtr_e"].index
            ),

        "same_test_students":
            splits["Xte_f"].index.equals(
                splits["Xte_e"].index
            ),

        "no_overlap":
            set(
                splits["Xtr_f"].index
            ).isdisjoint(
                splits["Xte_f"].index
            ),

        "summary":
            summary.to_dict(
                orient="records"
            )
    }

    manifest_path = REPORTS_DIR / "session22_manifest.json"

    with open(
        manifest_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            manifest,
            f,
            indent=4
        )

    return manifest

# ============================================================
# MAIN
# ============================================================

def main():

    X_full, X_early, y = load_datasets()

    validate_datasets(
        X_full,
        X_early,
        y
    )

    splits = create_splits(
        X_full,
        X_early,
        y
    )

    validate_splits(
        splits
    )

    check_reproducibility(
        X_full,
        y,
        splits
    )

    split_summary = create_split_summary(
        splits
    )

    validation_table = create_validation_table(
        splits
    )

    save_splits(
        splits
    )

    create_manifest(
        X_full,
        X_early,
        y,
        splits,
        split_summary
    )

    print("\nSESSION 22 COMPLETE\n")

    print(split_summary)

    print()

    print(validation_table)


if __name__ == "__main__":
    main()