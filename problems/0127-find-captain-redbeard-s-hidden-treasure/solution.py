def find_treasure(start_x: float) -> float:
    """
    Find the x-coordinate where f(x) = x^4 - 3x^3 + 2 is minimized.

  Returns:
        float: The x-coordinate of the minimum point.
    """
    # Calculus solution:
      # Find derivative
      # Set derivative = 0
      # Solve directly

    # f'(x) = 4x^3 - 9x^2
    # x^2(4x - 9) = 0
    # critical points: x = 0, 2.25
    critical_points = [0.0, 9.0 / 4.0]
    def f(x):
        return x**4 - 3*x**3 + 2
    return min(critical_points, key=f)

    # ---------------------------------------------------

    # Gradient descent: just like back propagation and gradient descent for finding minimized loss value for coefficients like W and B.
      # Guess x
      # Compute derivative
      # Move opposite to derivative
      # Repeat until convergence

    # f(x) = x^4 - 3x^3 + 2
    # df(x) = 4x^3 - 9x^2

    # x = start_x
    # lr = 0.01
    # while True:
    #     grad = 4*x**3 - 9*x**2
    #     if abs(grad) < 1e-6:
    #         break
    #     x = x - lr * grad
    # return x