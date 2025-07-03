# test_step16.py

from sparse_matrix import SparseMatrix

try:
    matrix1 = SparseMatrix.from_file("matrix1.txt")
    matrix2 = SparseMatrix.from_file("matrix2.txt")

    sum_matrix = matrix1 + matrix2

    print("Matrix 1:")
    print(matrix1)

    print("\nMatrix 2:")
    print(matrix2)

    print("\nSum of Matrix 1 and Matrix 2:")
    print(sum_matrix)

except Exception as e:
    print("Error during testing: {}".format(e))


