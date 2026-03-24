import numpy as np
# get matrix size
n, m = map(int, input("Enter rows and columns (e.g. 2 2): ").split())

# get matrix elements
arr = []
for i in range(n):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    arr.append(row)

# convert to NumPy array
arr = np.array(arr)

# print transpose
print("Transpose:")
print(np.transpose(arr))

# print flattened array
print("Flatten:")
print(arr.flatten())
