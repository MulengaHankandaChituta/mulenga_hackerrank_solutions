# hackerrank cartesian product challenge
from itertools import product

# read input lists
A = list(map(int, input("Enter elements of list A separated by space: ").split()))
B = list(map(int, input("Enter elements of list B separated by space: ").split()))

# compute cartesian product
cartesian_product = product(A, B)

# print tuples space-separated
print("Cartesian Product:")
print(*cartesian_product)