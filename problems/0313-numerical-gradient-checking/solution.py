import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    x = np.asarray(x, dtype=float)
    analytical_grad = np.asarray(analytical_grad, dtype=float)

    numerical_grad = np.zeros_like(x)

    for i in range(len(x)):
        x_plus = x.copy()
        x_minus = x.copy()

        x_plus[i] += epsilon
        x_minus[i] -= epsilon

        numerical_grad[i] = (
            f(x_plus) - f(x_minus)
        ) / (2 * epsilon)

    relative_error = (
        np.linalg.norm(numerical_grad - analytical_grad)
        / (np.linalg.norm(numerical_grad) + np.linalg.norm(analytical_grad))
    )

    return numerical_grad, relative_error