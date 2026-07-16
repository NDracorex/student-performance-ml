"""Reusable evaluation helpers for regression models."""
from typing import Dict, Sequence, Union
import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

# Define 1D Array-like type for annotation
ArrayLike1D = Union[Sequence[float], np.ndarray]

def eval_reg(
    y_true: ArrayLike1D,
    y_pred: ArrayLike1D,
) -> Dict[str, float]:
    """
    Calculate standard regression evaluation metrics.

    Parameters
    ----------
    y_true : ArrayLike1D
        Actual observed target values.
    y_pred : ArrayLike1D
        Predicted target values produced by a regression model.

    Returns
    -------
    dict
        Dictionary containing MAE, RMSE, and R2.

    Raises
    ------
    ValueError
        If the inputs are not one-dimensional, are empty, have different
        lengths, contain fewer than two observations, or contain non-finite values.
    """
    true_values = np.asarray(y_true, dtype=float)
    predicted_values = np.asarray(y_pred, dtype=float)

    if true_values.ndim != 1 or predicted_values.ndim != 1:
        raise ValueError("y_true and y_pred must be one-dimensional.")
    if true_values.size == 0 or predicted_values.size == 0:
        raise ValueError("y_true and y_pred cannot be empty.")
    if true_values.size != predicted_values.size:
        raise ValueError("y_true and y_pred must contain the same number of values.")
    if true_values.size < 2:
        raise ValueError("At least two observations are required to calculate R2.")
    if not np.all(np.isfinite(true_values)):
        raise ValueError("y_true contains missing or infinite values.")
    if not np.all(np.isfinite(predicted_values)):
        raise ValueError("y_pred contains missing or infinite values.")

    mse = mean_squared_error(true_values, predicted_values)

    return {
        "MAE": float(mean_absolute_error(true_values, predicted_values)),
        "RMSE": float(np.sqrt(mse)),
        "R2": float(r2_score(true_values, predicted_values)),
    }

"""
Classification-model evaluation utilities.

This module provides reusable helper functions for evaluating binary
classification models used in the student academic early-warning project.

Class convention:
1 = at-risk student
0 = student not currently classified as at risk.
"""

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)

def eval_clf(y_true, y_pred, y_proba=None):
    """
    Evaluate binary classification predictions.

    Parameters:
    -----------
    y_true : array-like
        Actual class labels. 1 means at risk, 0 means not at risk.
    y_pred : array-like
        Predicted class labels.
    y_proba : array-like, optional
        Predicted probabilities for the positive class (class 1).
        When provided, ROC-AUC is added to the returned metrics.

    Returns:
    --------
    dict: Dictionary containing accuracy, precision, recall, F1, and optional ROC-AUC.
    """
    # Enforce input length validations
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must contain the same number of observations.")
    if len(y_true) == 0:
        raise ValueError("The evaluation arrays must not be empty.")
    if y_proba is not None and len(y_true) != len(y_proba):
        raise ValueError("y_true and y_proba must contain the same number of observations.")

    results = {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
    }

    if y_proba is not None:
        results["roc_auc"] = float(roc_auc_score(y_true, y_proba))

    return results