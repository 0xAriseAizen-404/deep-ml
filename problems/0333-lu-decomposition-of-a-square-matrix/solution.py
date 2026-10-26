import numpy as np

def lu_decomposition(A: list) -> tuple:
    """
    Perform LU decomposition on a square matrix using Doolittle's method.

    Args:
        A: Square matrix as a list of lists

    Returns:
        tuple: (L, U) where L is lower triangular with 1s on diagonal, U is upper triangular, and A = L @ U
    """
    N = len(A)
    L = np.identity(N)
    U = np.zeros_like(L)

    # Doolittle Algorithm
    for i in range(N):
        # Compute U row by row
        for j in range(i, N):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

        # Compute L column by column
        for j in range(i + 1, N):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return (L, U)