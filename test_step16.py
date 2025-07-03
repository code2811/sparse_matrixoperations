# test_step16.py
# Author: Frida Ikirezi Kayiranga
# GitHub: https://github.com/code2811
# Description: Test script for adding two sparse matrices

from sparse_matrix import SparseMatrix

def main():
    try:
        matrix1 = SparseMatrix.from_file("sample_inputs/matrix1.txt")
        matrix2 = SparseMatrix.from_file("sample_inputs/matrix2.txt")

        sum_matrix = matrix1 + matrix2

        print("Matrix 1:")
        print(matrix1)

        print("\nMatrix 2:")
        print(matrix2)

        print("\nSum of Matrix 1 and Matrix 2:")
        print(sum_matrix)

    except Exception as e:
        print(f"Error during testing: {e}")

if __name__ == "__main__":
    main()


