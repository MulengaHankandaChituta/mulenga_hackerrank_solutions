import numpy as np

# take input
arr = list(map(int, input("Enter 9 space separated integers: ").split()))

# Convert to NumPy array
arr = np.array(arr)

# Reshape to 3x3
arr = arr.reshape(3, 3)

# print result
print(arr)
