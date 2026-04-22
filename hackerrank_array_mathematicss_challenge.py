import numpy as np

# Read dimensions
N, M = map(int, input("Enter N and M: ").split())

# Read array A
print("Enter elements of array A:")
A = []
for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)
# Read array B
print("Enter elements of array B:")
B = []
for i in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# Convert to NumPy arrays
A = np.array(A)
B = np.array(B)

# Perform operations
print("\nResults:\n")

print(A + B)
print(A - B)
print(A * B)
print(A // B)  # Integer division
print(A % B)
print(A ** B)
