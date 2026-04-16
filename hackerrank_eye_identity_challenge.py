import numpy as np

# Required for HackerRank output formatting
np.set_printoptions(legacy='1.13')

# take input
n, m = map(int, input("Enter rows and columns (e.g. 3 3): ").split())

# create the matrix
matrix = np.eye(n, m)

# print result
print(matrix)
