"""
SparseMatrix Class
Author: frida
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
                if line.strip():                      irow, col, value = map(int, line.split())
                    matrix.add_element(row, col, value)
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


def from_stream(cls, stream):
    lines = [line.strip() for line in stream.readlines() if line.strip()]
    if not lines[0].startswith("rows=") or not lines[1].startswith("cols="):
        raise ValueError("Input file has wrong format")

    num_rows = int(lines[0].split('=')[1])
    num_cols = int(lines[1].split('=')[1])
    matrix = cls(num_rows, num_cols)

    for line in lines[2:]:
        if not line.startswith("(") or not line.endswith(")"):
            raise ValueError("Invalid format")
        line = line[1:-1]
        parts = line.split(",")
        if len(parts) != 3:
            raise ValueError("Each entry must have 3 integers")
        row, col, val = map(int, parts)
        matrix.set_element(row, col, val)
    return matrix

