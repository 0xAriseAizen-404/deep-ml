import numpy as np

def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list.
    """
    n_samples = len(X)
    i = 0
    for _ in range(n_iter):
        ind = i % n_samples
        sample = X[ind].reshape(1, -1)
        target = y[ind]
        y_pred = sample @ weights
        errors = y_pred - target
        gradients = 2 * sample.T @ errors
        weights = weights - learning_rate * gradients
        i += 1
    return weights.flatten().tolist()