import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Your code here
    standardized_data = StandardScaler().fit_transform(data).round(4)
    normalized_data = MinMaxScaler().fit_transform(data).round(4)
    return standardized_data, normalized_data