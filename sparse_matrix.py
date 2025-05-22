"""
SparseMatrix Class
Author: Frida Ikirezi Kayiranga
Purpose: Load sparse matrix from file and manage its elements efficiently.
"""

class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}

    def add_element(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value

    def get_element(self, row, col):
        return self.data.get((row, col), 0)

    def set_element(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def __str__(self):
        result = []
        for i in range(self.rows):
            row_data = []
            for j in range(self.cols):
                row_data.append(str(self.get_element(i, j)))
            result.append(" ".join(row_data))
        return "\n".join(result)

    def to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(f"{self.rows} {self.cols}\n")
            for (row, col), value in self.data.items():
                f.write(f"{row} {col} {value}\n")

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            rows, cols = map(int, file.readline().split())
            matrix = cls(rows, cols)
            for line in file:
                if line.strip():
                    row, col, value = map(int, line.split())
                    matrix.add_element(row, col, value)
        return matrix

    @classmethod
    def from_stream(cls, stream):
        lines = [line.strip() for line in stream.readlines() if line.strip()]
        rows, cols = map(int, lines[0].split())
        matrix = cls(rows, cols)

        for line in lines[1:]:
            row, col, val = map(int, line.split())
            matrix.add_element(row, col, val)

        return matrix

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition.")
        
        result = SparseMatrix(self.rows, self.cols)
        keys = set(self.data.keys()) | set(other.data.keys())

        for key in keys:
            sum_value = self.get_element(*key) + other.get_element(*key)
            result.add_element(*key, sum_value)
        
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for subtraction.")
        
        result = SparseMatrix(self.rows, self.cols)
        keys = set(self.data.keys()) | set(other.data.keys())

        for key in keys:
            diff_value = self.get_element(*key) - other.get_element(*key)
            result.add_element(*key, diff_value)
        
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix multiplication not possible with these dimensions.")

        result = SparseMatrix(self.rows, other.cols)

        for (i, k1), v1 in self.data.items():
            for j in range(other.cols):
                v2 = other.get_element(k1, j)
                if v2 != 0:
                    current = result.get_element(i, j)
                    result.set_element(i, j, current + v1 * v2)

        return result

