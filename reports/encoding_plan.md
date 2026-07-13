# Encoding Plan

## Project

Predicting Student Academic Success Using Interpretable Machine Learning, Public Educational Data, and Prompt-Engineered Research Workflows

---

## Session

Session 11 – Categorical Variables

---

## Purpose

This document explains how categorical variables will be converted into numeric features before machine learning model training.

---

# Encoding Rules

## 1. Nominal Variables

Nominal variables have no natural order.

Example:

```text
teacher
health
services
other
at_home
```

Encoding method:

**One-Hot Encoding**

---

## 2. Binary Variables

Binary variables contain only two categories.

Example:

```text
yes
no
```

Encoding method:

**Binary Encoding**

Suggested mapping:

```
yes = 1
no = 0
```

---

## 3. Ordinal Variables

Ordinal variables have a meaningful order.

Examples:

```
low < medium < high
```

or

```
1 < 2 < 3 < 4
```

Encoding method:

Keep numeric ordinal variables as numeric features.

---

# Categorical Variable Encoding Plan

| Column | Example Values | Variable Type | Encoding Method | Reason |
|---|---|---|---|---|
| school | GP, MS | Binary/Nominal | Binary encoding | Two school categories; no ranking |
| sex | F, M | Binary/Nominal | Binary encoding | Two categories only |
| address | U, R | Binary/Nominal | Binary encoding | Urban and rural are labels |
| famsize | GT3, LE3 | Binary/Nominal | Binary encoding | Two family-size categories |
| Pstatus | A, T | Binary/Nominal | Binary encoding | Two parent-status categories |
| Mjob | teacher, health, services, other, at_home | Nominal | One-hot encoding | Job categories have no natural order |
| Fjob | teacher, health, services, other, at_home | Nominal | One-hot encoding | Job categories have no natural order |
| reason | course, home, reputation, other | Nominal | One-hot encoding | School-choice reasons are unordered labels |
| guardian | mother, father, other | Nominal | One-hot encoding | Guardian category has no ranking |
| schoolsup | yes, no | Binary | Binary encoding | Yes/no variable |
| famsup | yes, no | Binary | Binary encoding | Yes/no variable |
| paid | yes, no | Binary | Binary encoding | Yes/no variable |
| activities | yes, no | Binary | Binary encoding | Yes/no variable |
| nursery | yes, no | Binary | Binary encoding | Yes/no variable |
| higher | yes, no | Binary | Binary encoding | Yes/no variable |
| internet | yes, no | Binary | Binary encoding | Yes/no variable |
| romantic | yes, no | Binary | Binary encoding | Yes/no variable |

---

# Numeric Ordinal Variables

| Column | Variable Type | Encoding Decision | Reason |
|---|---|---|---|
| Medu | Ordinal | Keep numeric | Mother education level has ordered values |
| Fedu | Ordinal | Keep numeric | Father education level has ordered values |
| traveltime | Ordinal | Keep numeric | Travel-time levels are ordered |
| studytime | Ordinal | Keep numeric | Study-time levels are ordered |
| failures | Ordinal/Numeric | Keep numeric | Number of previous failures has numeric meaning |
| famrel | Ordinal | Keep numeric | Family relationship quality is ordered |
| freetime | Ordinal | Keep numeric | Free-time level is ordered |
| goout | Ordinal | Keep numeric | Going-out frequency is ordered |
| Dalc | Ordinal | Keep numeric | Workday alcohol consumption level is ordered |
| Walc | Ordinal | Keep numeric | Weekend alcohol consumption level is ordered |
| health | Ordinal | Keep numeric | Health status scale is ordered |

---

# High Cardinality Check

No major high-cardinality categorical variables were found.

Variables to monitor:

- Mjob
- Fjob
- reason
- guardian

These still have relatively few categories and are suitable for one-hot encoding.

---

# Reflection Question

**When would ordinal encoding mislead a model?**

Ordinal encoding is misleading when categories have no natural order. Assigning numbers to labels such as job type or guardian creates an artificial ranking that does not exist. Models may incorrectly interpret those numbers as meaningful distances. For unordered categories, one-hot encoding is the appropriate choice.

---

# Final Encoding Recommendation

1. Use binary encoding for two-category variables.
2. Use one-hot encoding for nominal variables.
3. Keep numeric ordinal variables as numeric.
4. Avoid ordinal encoding for unordered categories.
5. Monitor high-cardinality variables before one-hot encoding.