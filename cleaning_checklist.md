# Cleaning Checklist
## Project
Student Performance Prediction Using Machine Learning
## Session
Session 10: Missing Values and Duplicates
## Purpose
The purpose of this checklist is to document the data-quality checks completed
before preprocessing, feature engineering, and model development. The dataset was

checked for missing values and duplicate rows to make sure that downstream machine-
learning models are not affected by silent data-quality problems.

## 1. Missing Values Check
### Python Code Used
```python
print("Missing per column:")
print(df.isna().sum())
```
### Result
The missing-value check showed that all columns have zero missing values.

### Decision
No missing-value imputation is needed.

### Reason
Imputation is only needed when some values are missing and must be replaced or estimated. Since the
dataset contains no missing values, applying imputation would be unnecessary and could introduce
artificial information into the dataset.

## 2. Total Missing Values Check

### Python Code Used
```python
total_missing = df.isna().sum().sum()
print("Total missing values:", total_missing)
```
### Result
The total number of missing values was 0.

### Decision
The UCI claim of no missing values is confirmed for the dataset used in this project.

### Reason
Checking the total number of missing values gives a direct confirmation that the dataset is complete
across all columns and rows.

## 3. Duplicate Rows Check
### Python Code Used
```python
print("Duplicate rows:", df.duplicated().sum())
```

### Result
The duplicate-row check showed 0 duplicate rows.

### Decision
No duplicate rows need to be dropped.

### Reason
Duplicate rows can bias model training because repeated records may give extra weight to certain
observations. Since the duplicate count is 0, no duplicate-removal step is required.

## 4. Cleaning Decision Summary
| Data-Quality Issue | Result | Decision | Reason |
|---|---|---|---|
| Missing values | 0 | No imputation needed | The dataset is complete. |
| Duplicate rows | 0 | No rows dropped | No repeated records were found. |

## 5. Final Recommendation
No cleaning action is required for missing values or duplicate rows at this stage. The dataset is ready to
move forward to preprocessing and feature engineering.
However, this result should still be documented because confirming that no cleaning is needed is part of
a reproducible machine-learning workflow.