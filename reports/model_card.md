# Model Card: Student Academic Success Prediction

## Model Details
* **Model Type:** Ensemble Random Forest Regressor & Classifier (`RandomForestRegressor`, `RandomForestClassifier`)
* **Architecture Parameters:** 300 decision trees (`n_estimators=300`), default depth/split parameters optimized via 5-fold cross-validation (`RandomizedSearchCV`), fixed `random_state=42`.
* **Input Data:** UCI Student Performance Dataset (`student-mat.csv`), including demographic, social, and academic indicators.
* **Target Variables:**
  1. *Continuous Regression:* Final grade $G3$ (range 0–20).
  2. *Binary Classification:* At-Risk Student indicator ($1$ if $G3 < 10$, otherwise $0$).

---

## Intended Use & Application Scope
* **Primary Intended Use:** Academic early-warning decision support system designed to assist educators and academic advisors in identifying students who may benefit from early intervention prior to final term grading.
* **Out-of-Scope Uses:** * Automated grade determination or academic penalization.
  * High-stakes administrative actions (e.g., automated expulsion, scholarship revocation, or admissions decisions).

---

## Performance & Evaluation Summary
* **Regression Performance:** 5-fold cross-validated testing established stable $R^2$ performance ($pprox 0.80–0.84$) and low RMSE when evaluated on test partitions.
* **Classification Performance:** Ensemble models achieved top $F_1$ and ROC AUC performance for detecting at-risk students ($G3 < 10$).
* **Temporal Data Leakage Analysis:** Models trained without $G1$ and $G2$ maintain realistic early-warning validity prior to academic term grading, preventing temporal leakage.

---

## Interpretability & Key Predictors
* **Primary Features:** Feature importance analysis (MDI and test-set Permutation Importance) revealed that prior academic struggles (`failures`), behavioral tracking (`absences`), and academic commitment (`studytime`) are the dominant drivers of final grade outcomes.

---

## Ethical Considerations & Limitations
1. **Human-in-the-Loop Imperative:** Model outputs must serve purely as supportive recommendations for human educators and advisors, never as autonomous decision engines.
2. **Correlation vs. Causation:** Identified feature importances represent predictive correlations, not causal relationships. Changing a student's recorded variable will not automatically cause a grade improvement.
3. **Algorithmic Bias & Representation:** Demographic and socio-economic variables present in public educational datasets must be regularly audited to prevent reinforcing historical educational inequities or stereotypes.
4. **Contextual Limitations:** Model performance is conditioned on the training dataset distribution and must be re-calibrated before deployment in different institutional environments.
