import numpy as np

def calculate_correlation_matrix(X, Y=None):
    # Your code here
    corr_matrix = []
    if Y is not None:
        X = np.asarray(X).T
        Y = np.asarray(Y).T
        for i in range(len(X)):
            row = []
            for j in range(len(Y)):
                f1, f2 = X[i], Y[j]
                cov = np.sum((f1 - f1.mean()) * (f2 - f2.mean())) / (len(f1) - 1)
                row.append(cov / (f1.std(ddof=1) * f2.std(ddof=1)))
            corr_matrix.append(row)
    else:
        X = np.asarray(X).T
        for i in range(len(X)):
            row = []
            for j in range(len(X)):
                f1, f2 = X[i], X[j]
                cov = np.sum((f1 - f1.mean()) * (f2 - f2.mean())) / (len(f1) - 1)
                row.append(cov / (f1.std(ddof=1) * f2.std(ddof=1)))
            corr_matrix.append(row)
    return np.asarray(corr_matrix)