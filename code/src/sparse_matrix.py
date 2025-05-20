##!/usr/bin/env python3
"""
SparseMatrix Class
Author:frida
Purpose: Load sparse matrix from file and manage its elements efficiently.
"""


    def __init__(self, file_path=None, num_rows=None, num_cols=None):
        self.data = {}
        self.rows = 0
        self.cols = 0
        if file_path:
            self.load_from_file(file_path)
        else:
            self.rows = num_rows
            self.cols = num_cols

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
            self.rows = int(lines[0].strip().split('=')[1])
            self.cols = int(lines[1].strip().split('=')[1])

            for line in lines[2:]:
                line = line.strip()
                if not line or line[0] != '(' or line[-1] != ')':
                    raise ValueError("Input file has wrong format")
                parts = line[1:-1].split(',')
                if len(parts) != 3:
                    raise ValueError("Input file has wrong format")
                r, c, v = int(parts[0]), int(parts[1]), int(parts[2])
                self.data[(r, c)] = v
        except Exception as e:
            raise ValueError("Input file has wrong format") from e

    def get_element(self, r, c):
        return self.data.get((r, c), 0)

    def set_element(self, r, c, val):
        if val == 0 and (r, c) in self.data:
            del self.data[(r, c)]
        else:
            self.data[(r, c)] = val

    def __str__(self):
        entries = [f"({r}, {c}, {v})" for (r, c), v in self.data.items()]
        return f"rows={self.rows}\ncols={self.cols}\n" + "\n".join(entries)

