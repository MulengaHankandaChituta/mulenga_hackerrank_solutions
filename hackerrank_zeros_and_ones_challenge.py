import numpy as np

# take input (space-separated integers)
shape = tuple(map(int, input("Enter shape: ").split()))

# Create and print zeros array
zeros_array = np.zeros(shape, dtype=int)
print(zeros_array)

# Create and print ones array
ones_array = np.ones(shape, dtype=int)
print(ones_array)
