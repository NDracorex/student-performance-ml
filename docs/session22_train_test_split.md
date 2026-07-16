# Session 22: Reproducible Train/Test Splitting

## Deliverable
This session adds a reusable splitting utility to:
`src/preprocess.py`

The utility function is:
`split_modeling_scenarios(X_full, X_early, y, test_size=0.20, random_state=42)`

## Purpose
The utility creates directly comparable train/test partitions for:
1. The **Full-Information Scenario** (includes G1 and G2)
2. The **Early-Warning Scenario** (excludes G1 and G2)

The row indices are split exactly once and subsequently applied to both feature matrices and the target Series. This guarantees that both experiments contain the identical student population in their respective training and test sets, enabling clean, fair model comparisons.

## Returned Objects
The function returns a dictionary with the following keys:
- `Xtr_f`: Full-information training features
- `Xte_f`: Full-information test features
- `Xtr_e`: Early-warning training features
- `Xte_e`: Early-warning test features
- `ytr`: Shared training target (G3)
- `yte`: Shared test target (G3)