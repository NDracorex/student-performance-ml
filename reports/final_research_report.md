# Predicting Student Academic Success Using Interpretable Machine Learning, Public Educational Data, and Prompt-Engineered Research Workflows

**Author:** GSSRP Research Team  
**Institution:** Kean University  
**Date:** July 2026  

---

## Abstract
This study evaluates interpretable machine learning architectures to predict student final grades ($G3$) and identify at-risk students ($G3 < 10$) using the UCI Student Performance dataset. To simulate true early intervention and prevent temporal data leakage, models were evaluated under an early-warning configuration strictly excluding earlier period grades ($G1$ and $G2$). A broad spectrum of algorithms—ranging from linear baselines (Linear, Ridge, Lasso, Elastic Net) to distance/margin estimators (KNN, SVR), decision trees, ensemble methods (Random Forest, Extra Trees, Gradient Boosting, AdaBoost), and Multi-Layer Perceptron (MLP) neural networks—were systematically trained, cross-validated, and tuned. Random Forest and Gradient Boosting ensembles achieved superior predictive accuracy and classification $F_1$ scores. Feature importance analysis (MDI and test-set Permutation Importance) revealed that historical academic struggles (`failures`), behavioral tracking (`absences`), and study commitment (`studytime`) are the primary drivers of student academic success.

---

## 1. Introduction
Early identification of students at risk of academic failure allows educational institutions to deploy targeted support services prior to final grading. However, predictive modeling in education faces two major challenges: model interpretability and temporal data leakage. This project addresses both challenges by combining interpretable machine learning techniques with a strict leakage-aware research protocol.

### Research Questions
1. Which machine learning algorithms provide the most accurate predictions for student final grades ($G3$) and at-risk status ($G3 < 10$)?
2. What are the most influential academic, behavioral, and demographic features driving student performance?
3. How does excluding earlier period grades ($G1$ and $G2$) impact model accuracy versus early-warning validity?

---

## 2. Data & Feature Preprocessing
The study utilizes the public UCI Student Performance dataset (`student-mat.csv`), containing 395 student records across 33 variables.
* **Target Variables:**
  * *Regression:* Final grade $G3$ (continuous integer scale, 0–20).
  * *Classification:* Binary indicator `At-Risk` ($1$ if $G3 < 10$, $0$ if $G3 \ge 10$).
* **Leakage Prevention:** $G1$ and $G2$ were explicitly excluded from the early-warning predictor space.
* **Preprocessing Pipeline:** Categorical predictors were one-hot encoded (`OneHotEncoder`), and continuous features were scaled using `StandardScaler` inside scikit-learn `Pipeline` objects to prevent data leakage across validation folds.

---

## 3. Methodology
The modeling framework comprised three distinct phases:
1. **Regression Baselines & Ensembles:** Evaluated linear models, KNN, SVR, Decision Trees, Random Forests, Extra Trees, Gradient Boosting, and MLP regressors.
2. **Classification Models:** Evaluated Logistic Regression, KNN, SVM, Naive Bayes, Decision Trees, Random Forests, Boosting, and MLP classifiers.
3. **Cross-Validation & Hyperparameter Tuning:** Applied 5-fold cross-validation (`cross_val_score`) and systematic grid/randomized search (`GridSearchCV`, `RandomizedSearchCV`) to optimize ensemble architectures.

---

## 4. Results
* **Regression Leaderboard:** Ensembles (Random Forest, Gradient Boosting, Extra Trees) and penalized linear baselines (Elastic Net) demonstrated superior generalization, achieving test RMSE values between 2.03 and 2.17.
* **Classification Leaderboard:** Gradient Boosting and Random Forest Classifiers achieved top performance, leading in test $F_1$ score and ROC AUC for at-risk student detection.
* **Cross-Validation Stability:** 5-fold cross-validation confirmed that model performance remains consistent across data folds, ruling out split-dependent artifacts.

---

## 5. Model Interpretation & Key Predictors
* **Built-in Tree Importances (MDI):** Identified `failures` (past class failures), `absences` (school absences), and `studytime` (weekly study time) as the most critical features.
* **Test-Set Permutation Importance:** Confirmed that shuffling `failures` and `absences` caused the greatest deterioration in test-set RMSE, validating model dependency on behavioral and historical performance metrics on unseen data.

---

## 6. Leakage-Aware Findings & Discussion
Comparing models trained with $G1$/$G2$ versus without $G1$/$G2$ highlighted a critical trade-off:
* Including $G1$ and $G2$ increases predictive accuracy ($R^2$ improves substantially).
* However, including $G1$/$G2$ constitutes temporal data leakage, as term grades are unavailable during early intervention periods.
* Excluding $G1$ and $G2$ establishes a realistic early-warning system that operates effectively prior to term grading.

---

## 7. Ethical Limitations & Responsible AI Governance
* **Supportive Role:** Model predictions must serve as advisory insights for educators, never as autonomous decision engines for penalization or grading.
* **Predictive vs. Causal:** Feature importances reflect statistical correlations, not direct causal mechanisms.
* **Fairness & Bias:** Demographic variables must be continually audited to prevent automated bias or stereotyping.

---

## 8. Conclusion
This study demonstrates that interpretable ensemble machine learning models can effectively identify at-risk students prior to final term grading without relying on leaked period grades. Random Forest and Gradient Boosting models offer an optimal balance of predictive power and model transparency, establishing a robust foundation for early-warning educational interventions.

---

## References
1. Cortez, P., & Silva, A. M. (2008). *Using Data Mining to Predict Secondary School Student Performance*. EUROSIS.
2. Breiman, L. (2001). *Random Forests*. Machine Learning, 45(1), 5-32.
3. Pedregosa, F., et al. (2011). *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 12, 2825-2830.
