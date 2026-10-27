import numpy as np

def cholesky_decomposition(A):
    """
    Perform Cholesky decomposition on a symmetric positive-definite matrix.
    
    Args:
        A: A symmetric positive-definite matrix (2D list or numpy array)
    
    Returns:
        L: Lower triangular matrix such that A = L @ L.T as a 2D list,
           or -1 if decomposition is not possible
    """
    # To perform Cholesky Decomposition, A = L.L^T
    # Here, A should be Symmetric meaning A = A^T
    # A should be Positive-Definite, meaning all eigenvalues are positive, xT*Ax > 0 for every non-zero vector x
    A = np.asarray(A)
    m, n = len(A), len(A[0])
    if A.size == 0: # Empty Matrix
        return -1
    if m != n: # Not a Square Matrix
        return -1
    if not np.allclose(A, A.T) or not np.all(np.linalg.eigvalsh(A) > 0): # Not a Symmetric Positive-Definite Matrix
        return -1
    L = np.zeros_like(A)
    for i in range(len(A)):
        for j in range(i + 1):
            if i == j:
                L[i][i] = np.sqrt(A[i][i] - sum(L[i][k]**2 for k in range(i)))
            else:
                L[i][j] = (A[i][j] - sum(L[i][k] * L[j][k] for k in range(j))) / L[j][j]
    return L.tolist()