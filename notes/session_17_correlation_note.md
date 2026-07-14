# Session 17: Correlation Analysis

## Objective

Compute and visualize Pearson correlations among the numeric variables and identify
the variables most strongly associated with the target variable G3.

---

## Correlation Heatmap

The correlation heatmap was generated using the Pearson correlation coefficient and
saved as:

`figures/correlation_heatmap.png`

---

## Top Correlations with G3

| Rank | Feature | Correlation | Direction |
|------|---------|------------:|-----------|
| 1 | G2 | 0.904868 | Positive |
| 2 | G1 | 0.801468 | Positive |
| 3 | failures | -0.360415 | Negative |
| 4 | Medu | 0.217147 | Positive |
| 5 | age | -0.161579 | Negative |

---

## Interpretation

- The strongest predictor of G3 was **G2**.
- G1 and G2 showed strong positive correlations with G3 because they represent
  earlier grades earned during the same course.
- Positive correlations indicate that higher values of the feature tend to be
  associated with higher final grades.
- Negative correlations indicate that higher values of the feature tend to be
  associated with lower final grades.

---

## Data Leakage Discussion

Although G1 and G2 are highly predictive of G3, they may not be appropriate for an
early-warning model because these grades are not available early in the semester.

Two modeling scenarios should be considered:

- **Full-information model:** includes G1 and G2.
- **Early-warning model:** excludes G1 and G2.

Comparing both models will show how much predictive performance depends on prior
grade information.

---

## Methodological Note

The correlations shown are Pearson correlation coefficients. Correlation measures
the strength and direction of a linear relationship between variables but does not
imply causation.

---

## Output Artifact

- `figures/correlation_heatmap.png`