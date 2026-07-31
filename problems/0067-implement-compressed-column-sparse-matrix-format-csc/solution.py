def compressed_col_sparse_matrix(dense_matrix):
    """
    Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

    :param dense_matrix: List of lists representing the dense matrix
    :return: Tuple of (values, row indices, column pointer)
    """
    values = []
    row_indices = []
    column_pointers = []
    for col in range(len(dense_matrix[0])):
        firstOne = True
        for i, row in enumerate(dense_matrix):
            if row[col] != 0:
                if firstOne:
                    column_pointers.append(len(values))
                    firstOne = False
                values.append(row[col])
                row_indices.append(i)
    if len(column_pointers) == 0:
        column_pointers = [0] * len(dense_matrix)
    column_pointers.append(len(values))
    return (values, row_indices, column_pointers)
