import numpy as np

def divide_on_feature(X, feature_i, threshold):
    return [
    [row for row in X if row[feature_i] >= threshold],
    [row for row in X if row[feature_i] < threshold]
    ]