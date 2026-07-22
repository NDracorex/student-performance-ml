# Prompt-Engineered Research Summary Notes
**Project:** Predicting Student Academic Success Using Interpretable Machine Learning  
**Dataset:** UCI Student Performance Dataset (student-mat.csv)  

---

## 1. Executive Summary & Study Purpose
This research study evaluates machine learning models to identify at-risk students and predict final academic performance ($G3$) using public educational data. To ensure real-world utility, early-warning models strictly exclude earlier period grades ($G1$ and $G2$) to avoid temporal data leakage.

## 2. Model Performance Leaderboards
* **Regression Modeling:** Evaluated baselines (Linear, Ridge, Lasso, Elastic Net), distance/tree estimators (KNN, SVR, Decision Trees), and ensembles (Random Forest, Gradient Boosting, Extra Trees, MLP). Regressors were ranked by test RMSE on `reports/regression_leaderboard.csv`.
* **Classification Modeling:** Transformed the problem to detect at-risk students ($G3 < 10$). Evaluated Logistic Regression, KNN, SVM, Naive Bayes, Decision Trees, Random Forests, Boosting, and MLP. Ranked by test $F_1$ score on `reports/classification_leaderboard.csv`.

## 3. Key Predictors & Interpretability Findings
* **Feature Importance:** Random Forest MDI importances identified historical academic struggles (`failures`), behavioral tracking (`absences`), and academic commitment (`studytime`) as primary drivers.
* **Permutation Importance:** Model-agnostic test-set permutation importance confirmed reliance on behavioral and academic history features, showing consistency with built-in tree importances.

## 4. Methodological Insights & Research Conclusions
* **Temporal Leakage Analysis:** Including $G1$ and $G2$ artificially boosts predictive accuracy but introduces temporal leakage. Excluding $G1$ and $G2$ establishes a realistic early-warning system prior to grading.
* **Tuning & Validation:** 5-fold cross-validation (`cross_val_score`) verified that ensemble performance is statistically stable across partitions rather than driven by a single lucky split.
