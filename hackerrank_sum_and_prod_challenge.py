import numpy as np

# Get the dimensions of the array
N, M = map(int, input("Enter N and M: ").split())

# Get the array elements
my_array = np.array([
    list(map(int, input(f"Enter row {i + 1}: ").split()))
    for i in range(N)
])

# calculate the sum along axis 0
sum_result = np.sum(my_array, axis=0)

# Calculate the product of the sum
result = np.prod(sum_result)

# Display results
print("\nArray:")
print(my_array)

print("\nSum along axis 0:")
print(sum_result)

print("\nProduct of the sum:")
print(result)

