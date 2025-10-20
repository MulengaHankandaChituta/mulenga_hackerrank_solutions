# hackerrank string permutations challenge

from itertools import permutations

# read input string and size
s, k = input("Enter string and size (e.g., HACK 2): ").split()
k =  int(k)

# sorting the string for lexicographic order
s = sorted(s)

# generate permutations of size k
print(f"Permutations of size {k}:")
for p in permutations(s, k):
    print(''.join(p))