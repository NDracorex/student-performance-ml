"""
Session 22 - Preprocessing Tests

Tests verify:
- Data loading
- Encoding correctness
- Leakage prevention
- Feature/target separation
- Dataset integrity
"""


from pathlib import Path
import pandas as pd


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "early_warning_dataset.csv"
)

X_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "X_early.csv"
)

Y_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "y_early.csv"
)


def test_processed_dataset_exists():
    """
    Confirm processed dataset was created.
    """

    assert DATA_PATH.exists(), (
        "early_warning_dataset.csv missing"
    )


def test_feature_file_exists():

    assert X_PATH.exists(), (
        "X_early.csv missing"
    )


def test_target_file_exists():

    assert Y_PATH.exists(), (
        "y_early.csv missing"
    )


def test_dataset_loads():

    df = pd.read_csv(DATA_PATH)

    assert isinstance(df, pd.DataFrame)

    assert len(df) > 0


def test_feature_target_row_alignment():

    X = pd.read_csv(X_PATH)

    y = pd.read_csv(Y_PATH)

    assert len(X) == len(y), (
        "Feature and target rows do not match"
    )


def test_no_grade_leakage():

    """
    G1 and G2 are future grade information.
    They cannot be used in early-warning prediction.
    """

    X = pd.read_csv(X_PATH)

    forbidden_columns = [
        "G1",
        "G2",
        "G3"
    ]

    for col in forbidden_columns:
        assert col not in X.columns, (
            f"Leakage detected: {col}"
        )


def test_target_is_G3():

    y = pd.read_csv(Y_PATH)

    assert list(y.columns) == ["G3"], (
        "Target column should be G3"
    )


def test_no_duplicate_features():

    X = pd.read_csv(X_PATH)

    duplicates = (
        X.columns[
            X.columns.duplicated()
        ]
    )

    assert len(duplicates) == 0, (
        f"Duplicate columns found: {duplicates}"
    )


def test_no_missing_values():

    X = pd.read_csv(X_PATH)

    missing = X.isna().sum().sum()

    assert missing == 0, (
        f"Missing values detected: {missing}"
    )


def test_encoding_created_numeric_features():

    """
    Machine learning models require numeric inputs.
    """

    X = pd.read_csv(X_PATH)

    non_numeric = (
        X.select_dtypes(
            exclude="number"
        ).columns
    )

    assert len(non_numeric) == 0, (
        f"Non-numeric columns remain: {non_numeric}"
    )