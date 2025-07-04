
        
# sparse_matrix.py
"""
SparseMatrix Class
-------------------
Author: Frida Ikirezi Kayiranga (GitHub: @code2811)
Defines a lightweight data structure and operations for sparse matrices.
"""

class SparseMatrix:
    def __init__(self, file_path=None, num_rows=0, num_cols=0, data=None):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.data = data if data else {}
        if file_path:
            self._load_from_file(file_path)
    
    def _load_from_file(self, file_path):
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            if not lines[0].startswith("rows=") or not lines[1].startswith("cols="):
                raise ValueError("Input file has wrong format")
            self.num_rows = int(lines[0].split('=')[1])
            self.num_cols = int(lines[1].split('=')[1])
            for line in lines[2:]:
                if not (line.startswith('(') and line.endswith(')')):
                    raise ValueError("Invalid line format: " + line)
                parts = line[1:-1].split(',')
                if len(parts) != 3:
                    raise ValueError("Line must have 3 elements: " + line)
                try:
                    r, c, v = int(parts[0].strip()), int(parts[1].strip()), int(parts[2].strip())
                    if v != 0:
                        self.data[(r, c)] = v
                except ValueError:
                    raise ValueError("Invalid integer values: " + line)
    
    @classmethod
    def from_file(cls, file_path):
        """Create a SparseMatrix from a file"""
        return cls(file_path=file_path)
    
    def get(self, row, col):
        return self.data.get((row, col), 0)
    
    def set(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]
    
    def add(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix sizes must match for addition.")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        result.data = self.data.copy()
        for (r, c), v in other.data.items():
            result.set(r, c, result.get(r, c) + v)
        return result
    
    def subtract(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix sizes must match for subtraction.")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        result.data = self.data.copy()
        for (r, c), v in other.data.items():
            result.set(r, c, result.get(r, c) - v)
        return result
    
    def multiply(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrix dimensions do not match for multiplication.")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        for (i, k), v in self.data.items():
            for j in range(other.num_cols):
                val = other.get(k, j)
                if val != 0:
                    result.set(i, j, result.get(i, j) + v * val)
        return result
    
    def get_dimensions(self):
        return self.num_rows, self.num_cols
    
    def get_non_zero_count(self):
        return len(self.data)
    
    def save_to_file(self, output_path):
        with open(output_path, 'w') as f:
            f.write("rows={}\n".format(self.num_rows))
            f.write("cols={}\n".format(self.num_cols))
            for (r, c), v in sorted(self.data.items()):
                f.write("({}, {}, {})\n".format(r, c, v))
    
    def __str__(self):
        output = ["rows={}".format(self.num_rows), "cols={}".format(self.num_cols)]
        for (r, c), v in sorted(self.data.items()):
            output.append("({}, {}, {})".format(r, c, v))
        return '\n'.join(output)
    
    # Operator overloads for convenience
    def __add__(self, other):
        return self.add(other)
    
    def __sub__(self, other):
        return self.subtract(other)
    
    def __mul__(self, other):
        return self.multiply(other)
           
       

      

    
      
            

    
        
