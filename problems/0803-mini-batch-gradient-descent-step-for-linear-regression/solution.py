import numpy as np

def mini_batch_gd_step(X: np.ndarray, y: np.ndarray, weights: np.ndarray, bias: float, batch_indices: list, lr: float) -> np.ndarray:
    """
    Perform one mini-batch gradient descent update step for linear regression with MSE loss.
    Returns a 1D array of length D+1: updated weights followed by updated bias.
    """
    X_batch = X[batch_indices]
    y_batch = y[batch_indices].reshape(-1, 1)
    weights = weights.reshape(-1, 1)

    y_pred = X_batch @ weights + bias
    errors = y_pred - y_batch

    m = X_batch.shape[0]
    grad_w = (2 / m) * X_batch.T @ errors
    grad_b = (2 / m) * np.sum(errors)

    weights = weights - lr * grad_w
    bias = bias - lr * grad_b

    return np.concatenate([weights.flatten(), [bias]])