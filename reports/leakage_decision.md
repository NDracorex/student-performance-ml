# Leakage-Decision Note

## Session Information
- **Program:** GSSRP 2026
- **Project:** Predicting Student Academic Success Using Interpretable Machine Learning
- **Session:** 18 of 48 
- **Topic:** Data-leakage discussion
- **Target variable:** G3 (Final Grade)
- **Prior-grade predictors under review:** G1 (First-period grade) and G2 (Second-period grade)

## 1. Decision Purpose
This note documents the project decision regarding whether the first-period grade, G1, and second-period grade, G2, should be included when predicting the final grade, G3. 
The decision is based on three considerations:
1. The predictive value of G1 and G2.
2. The time at which G1 and G2 become available.
3. The intended operational purpose of the model.

## 2. Correlation Evidence
The Session 18 correlation analysis produced the following results:
- **Correlation between G1 and G3:** 0.801
- **Correlation between G2 and G3:** 0.905 

These results indicate that prior course grades contain substantial information about the final grade. Including G1 and G2 is therefore expected to improve predictive performance. However, correlation strength alone does not determine whether a predictor is appropriate. The predictor must also be available at the intended prediction time. Crucially, correlation represents an association rather than proof of causation.

## 3. Data-Leakage Interpretation
Data leakage occurs when a model uses information that would not realistically be available when the prediction is supposed to be made. G1 and G2 are not automatically leakage variables in every modeling context:
- They are **legitimate** predictors when the model is used after those grades have already been recorded (full-information context).
- They are **inappropriate** for a beginning-of-course early-warning model because they do not exist at the required prediction time.

The project will therefore utilize two separately defined modeling scenarios.

## 4. Scenario 1: Full-Information Model
- **Decision:** Include G1 and G2.
- **Purpose:** Measure maximum predictive performance when prior course grades are fully known.
- **Prediction Time:** Assumed to occur near the end of the term, after both G1 and G2 have been recorded.
- **Predictors Included:** G1, G2, Demographic variables, Behavioral variables, Family-related variables, School-support variables, Academic-history variables.
- **Expected Performance:** Higher predictive accuracy and lower error rates, serving as our baseline "best-case scenario" benchmark.
- **Limitation:** Highly limited early-warning value; predictions occur too late in the academic term to implement comprehensive student recovery plans.

## 5. Scenario 2: Early-Warning Model
- **Decision:** Exclude G1 and G2.
- **Purpose:** Identify students at risk early in the academic term before any prior exam grades are available.
- **Prediction Time:** Near the start of the course.
- **Excluded Variables:** G1, G2.
- **Eligible Predictors:** Study time, previous academic failures, family support, school support, travel time, internet access, educational aspirations, social and behavioral factors.
- **Expected Performance:** Lower statistical predictive accuracy due to the exclusion of two heavily informative grade parameters.
- **Value:** Exceptionally high operational value; enables tutors and advisors enough lead time to implement supportive interventions.

## 6. Scenario Comparison

| Criterion | Full-Information Model | Early-Warning Model |
| :--- | :--- | :--- |
| **Includes G1** | Yes | No |
| **Includes G2** | Yes | No |
| **Prediction Timing** | After prior grades are recorded | Before prior grades are recorded |
| **Expected Accuracy** | Higher | Lower |
| **Time for Intervention** | Less | More |
| **Primary Purpose** | Maximum predictive performance | Early risk identification |
| **Leakage Interpretation** | Valid when used after G1 and G2 exist | G1 and G2 excluded to match early prediction timing |
| **Main Limitation** | Limited early-warning value | Lower statistical performance |

## 7. Evaluation Plan
The two scenarios will be trained and evaluated completely separately using consistent preprocessing, random seeds, split protocols, and cross-validation procedures. Regression performance will be evaluated on standard metrics:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared ($R^2$)

Crucially, the model with the highest statistical accuracy will not automatically be treated as the most useful model. Practical operational timing will be weighted equally.

## 8. Final Project Decision
The project will officially adopt a **two-scenario design**:
1. **Full-information scenario:** Include G1 and G2.
2. **Early-warning scenario:** Exclude G1 and G2.

The results will be reported separately because they answer fundamentally different research and operational questions.