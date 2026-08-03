import numpy as np

# Get the number of rows and columns
n, m = map(int, input("Enter rows and columns: ").split())

# Get the array values
print("Enter the array rows:")

my_array = np.array([list(map(int, input().split())) for _ in range(n)])

# Find the minimum value along axis 1 (row-wise)
min_values = np.min(my_array, axis=1)

# Find the maximum value of minimum values
result = np.max(min_values)

# Display results
print("\nArray:")
print(my_array)

print("\nMinimum values along axis 1:")
print(min_values)

print("\nMaximum of the minimum values:")
print(result)
