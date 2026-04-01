import numpy as np

# take input
n, m, p = map(int, input("Enter n m p: ").split())

# First array
print("Enter first array: ")
array1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    array1.append(row)

# second array
print("Enter second array: ")
array2 = []
for _ in range(m):
    row = list(map(int, input().split()))
    array2.append(row)

# convert to  numpy arrays
array1 = np.array(array1)
array2 = np.array(array2)

# concatenate
result = np.concatenate((array1, array2), axis=0)

# output
print("Result: ")
print(result)
               
