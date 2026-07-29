import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape

    output_matrix = []

    mat_height = input_height + padding + padding
    mat_width = input_width + padding + padding
    matrix = [[0] * mat_width for _ in range(mat_height)]
    for i in range(input_height):
        for j in range(input_width):
            matrix[padding+i][padding+j] = input_matrix[i][j]
    matrix = np.asarray(matrix)
    
    output_matrix = []
    for i in range(0, mat_height - kernel_height + 1, stride):
        l = []
        for j in range(0, mat_width - kernel_width + 1, stride):
            C = matrix[i:i+kernel_height, j:j+kernel_width] * kernel
            l.append(C.sum())
        output_matrix.append(l)
    return (np.round(output_matrix, 4)).tolist()