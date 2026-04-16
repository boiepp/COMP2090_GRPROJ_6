class Matrix:
    def __init__(self, data):
        if not data or not data[0]:
            raise ValueError("Matrix cannot be empty")
        self.data = [row[:] for row in data]
        self.rows = len(data)
        self.cols = len(data[0])
        
        for row in data:
            if len(row) != self.cols:
                raise ValueError("All rows must have same length")
    
    def get(self, row, col):
        return self.data[row][col]
    
    def set(self, row, col, value):
        self.data[row][col] = value
    
    def transpose(self):
        transposed = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(transposed)
    
    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)
    
    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for subtraction")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)
    
    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions must match: cols of A must equal rows of B")
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)
    
    def scalar_multiply(self, scalar):
        result = [[self.data[i][j] * scalar for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)
    
    def display(self):
        for row in self.data:
            print("  ".join(f"{val:6}" for val in row))
    
    def to_list(self):
        return [row[:] for row in self.data]


if __name__ == "__main__":
    print("=" * 50)
    print("Matrix Data Structure Demo")
    print("=" * 50)
    
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    
    print("\nMatrix A:")
    m1.display()
    print("\nMatrix B:")
    m2.display()
    
    print("\nA + B:")
    m1.add(m2).display()
    
    print("\nA - B:")
    m1.subtract(m2).display()
    
    print("\nTranspose of A:")
    m1.transpose().display()
    
    print("\nA * 3:")
    m1.scalar_multiply(3).display()
    
    m3 = Matrix([[1, 2], [3, 4], [5, 6]])
    m4 = Matrix([[7, 8, 9], [10, 11, 12]])
    print("\nMatrix C (3x2):")
    m3.display()
    print("\nMatrix D (2x3):")
    m4.display()
    print("\nC * D (3x3):")
    m3.multiply(m4).display()
