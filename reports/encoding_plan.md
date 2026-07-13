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

| Column | Variable Type | Encoding | Reason |
|----------|--------------|-----------|---------|
| school | Binary | Binary | Two schools |
| sex | Binary | Binary | Two categories |
| address | Binary | Binary | Urban/Rural labels |
| famsize | Binary | Binary | Two family-size groups |
| Pstatus | Binary | Binary | Parent status |
| Mjob | Nominal | One-Hot | No ranking |
| Fjob | Nominal | One-Hot | No ranking |
| reason | Nominal | One-Hot | No ranking |
| guardian | Nominal | One-Hot | No ranking |
| schoolsup | Binary | Binary | Yes/No |
| famsup | Binary | Binary | Yes/No |
| paid | Binary | Binary | Yes/No |
| activities | Binary | Binary | Yes/No |
| nursery | Binary | Binary | Yes/No |
| higher | Binary | Binary | Yes/No |
| internet | Binary | Binary | Yes/No |
| romantic | Binary | Binary | Yes/No |

---

# Numeric Ordinal Variables

| Column | Decision |
|----------|-----------|
| Medu | Keep numeric |
| Fedu | Keep numeric |
| traveltime | Keep numeric |
| studytime | Keep numeric |
| failures | Keep numeric |
| famrel | Keep numeric |
| freetime | Keep numeric |
| goout | Keep numeric |
| Dalc | Keep numeric |
| Walc | Keep numeric |
| health | Keep numeric |

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