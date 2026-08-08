import numpy as  np

n = int(input("Enter the size of the matrices: "))

print("Enter matrix A:")

A = np.array([list(map(int, input().split())) for _ in range(n)])

print("Enter matrix B:")
B = np.array([list(map(int, input().split())) for _ in range(n)])

result = np.dot(A, B)

print("\nMatrix multiplication:")
print(result)

