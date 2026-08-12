import numpy as np

# Read matrix size
n = int(input("Enter matrix size: "))

# read the matrix
matrix = []

for i in range(n):
    row = list(map(float, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

# convert to NumPy array
matrix = np.array(matrix)

# calculate determinant
determinant = np.linalg.det(matrix)

# display result
print("Determinant:", round(determinant, 2))
