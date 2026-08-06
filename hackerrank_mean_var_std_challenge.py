import numpy as np

# Read the dimensions
n, m = map(int, input().split())

# read the array
arr = np.array([list(map(int, input().split())) for _ in range(n)])

# Print the mean along axis 1
print(np.mean(arr, axis=1))

# Print the variance along axis 0
print(np.var(arr, axis=0))

# Print the standard deviation of the entire array
print(np.std(arr).round(11))
