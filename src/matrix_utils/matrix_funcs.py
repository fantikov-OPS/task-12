from .matrix_classes import Matrix

def _check_matrix(matrix):
    if not isinstance(matrix, Matrix):
        raise TypeError("Нужна матрица")

def matrix_max(matrix):
    _check_matrix(matrix)
    return max(max(row) for row in matrix.data)

def matrix_min(matrix):
    _check_matrix(matrix)
    return min(min(row) for row in matrix.data)

def matrix_sum(matrix):
    _check_matrix(matrix)
    return sum(sum(row) for row in matrix.data)