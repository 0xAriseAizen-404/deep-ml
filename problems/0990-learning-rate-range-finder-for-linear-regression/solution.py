import numpy as np

def lr_range_finder(X, y, w0, a, b, n_steps):
    """
    Sweep learning rate from 10**a to 10**b over n_steps full-batch GD updates
    on a linear regression model (no bias). Return the list of MSE losses after
    each update.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1, 1)
    w0 = np.asarray(w0, dtype=float).reshape(-1, 1)
    
    N = X.shape[0]
    losses = []
    for k in range(n_steps):
        if n_steps == 1:
            lr = 10 ** a
        else:
            lr = 10 ** (a + (b - a) * k / (n_steps - 1))
        y_pred = X @ w0
        errors = y_pred - y
        # update step
        grad = (2 / N) * X.T @ errors
        w0 = w0 - lr * grad
        # loss with updated weights
        loss = np.mean((X @ w0 - y) ** 2)
        losses.append(loss.item())
    return losses