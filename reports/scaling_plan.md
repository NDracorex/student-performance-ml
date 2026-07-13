# Scaling Plan
## Session 12: Numerical Variables
## Project Context
This project predicts student academic success using public educational data and
interpretable machine-learning workflows. Session 12 focuses on identifying
numerical variables and deciding when numeric feature scaling is required.
## Purpose
The purpose of this scaling plan is to document which numerical features should be
scaled before model training. Some machine-learning models are sensitive to the
size and range of numeric variables. Other models are less affected by feature
scaling.
This note records:
- Why scaling matters
- Which models require scaling
- Which models usually do not require scaling
- How scaling should be handled in the project pipeline
## Python Code Used
The numeric columns were reviewed using the following Python code:
```python
num_cols = df.select_dtypes(include="number").columns.tolist()
print(df[num_cols].agg(["min", "max", "mean"]).T)
```
This code identifies all numeric columns and reports each column’s:
- Minimum value
- Maximum value
- Mean value
These summary statistics help determine whether numerical variables are on very
different scales.
## Why Scaling Matters
Scaling matters because some models compare observations using distances,
gradients, margins, or coefficients.

If one numeric feature has a much larger range than another feature, the larger-
scale feature can dominate the model even if it is not more important.

For example, if one variable ranges from 0 to 4 and another variable ranges from 0
to 100, distance-based models may give too much influence to the variable with the
larger range.
## Models That Require Scaling
| Model | Requires Scaling? | Reason |
|---|---:|---|
| Linear Regression | Yes | Linear regression can be affected when variables have
very different numeric ranges, especially when regularization is used. |
| Logistic Regression | Yes | Logistic regression uses coefficient estimation and
optimization. Scaling helps convergence and coefficient stability. |
| K-Nearest Neighbors | Yes | KNN is distance-based. Features with larger ranges
can dominate distance calculations if scaling is not applied. |
| Support Vector Machine | Yes | SVM depends on margins and distances. Scaling
helps prevent one feature from dominating the margin. |
| Neural Network | Yes | Neural networks use gradient-based optimization. Scaled
inputs usually improve training stability. |
## Models That Usually Do Not Require Scaling
| Model | Requires Scaling? | Reason |
|---|---:|---|
| Decision Tree | No | Decision trees split data using thresholds. They depend
mainly on ordering, not the absolute scale of values. |
| Random Forest | No | Random forests are collections of decision trees, so they
are usually not sensitive to feature scale. |
| Gradient Boosting | No | Tree-based boosting models also use threshold-based
splits and usually do not require scaling. |
## Interpretation
The project includes a mix of model families. Linear, distance-based, margin-based,
and neural-network models should use scaled numeric features. Tree-based models
generally do not need scaling because their split decisions are based on
thresholds.
Scaling should not be applied blindly to every model. Instead, the project should
use model-specific preprocessing pipelines.
## Recommended Pipeline Approach
The project should use two preprocessing strategies.
### Pipeline 1: Scaled Numeric Features
Use this pipeline for:
- Linear Regression
- Logistic Regression
- K-Nearest Neighbors
- Support Vector Machine
- Neural Network
Recommended numeric preprocessing:
```python
StandardScaler()
```
### Pipeline 2: Unscaled Numeric Features
Use this pipeline for:
- Decision Tree
- Random Forest
- Gradient Boosting
Recommended numeric preprocessing:
```python
passthrough
```
## Data Leakage Warning
The scaler must be fitted only on the training data. The fitted scaler should then
be applied to validation and test data.
Correct approach:
1. Split the data into training and testing sets.
2. Fit the scaler on the training data only.
3. Transform the training data using the fitted scaler.
4. Transform the test data using the same fitted scaler.
This prevents information from the test set from leaking into the training process.
## Reflection Question
### Why do tree-based models care less about feature scaling than KNN or SVM?
Tree-based models care less about feature scaling because they split the data using
threshold rules. For example, a decision tree may split students based on whether
study time is less than or equal to a certain value. The model mainly depends on
the ordering of values, not the exact scale of the numbers.
KNN and SVM are more sensitive to scaling. KNN uses distance calculations to
compare observations. If one feature has a much larger numeric range than another
feature, that feature can dominate the distance calculation. SVM is also sensitive
to scale because it depends on margins and distances between observations.
Therefore, scaling is usually important for KNN and SVM, but it is usually not
required for decision trees, random forests, or tree-based gradient boosting
models.
## Final Scaling Decision
The project will use scaling for models that are sensitive to numeric feature
ranges:
- Linear Regression
- Logistic Regression
- KNN
- SVM
- Neural Networks
The project will not require scaling for tree-based models:
- Decision Tree
- Random Forest
- Gradient Boosting
The final modeling workflow should use scikit-learn `Pipeline` and
`ColumnTransformer` so that each model receives the correct preprocessing.