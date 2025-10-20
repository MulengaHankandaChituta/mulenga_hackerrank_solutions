# hackerrank string combinations challenge

from itertools import combinations

# read input string and max size
s, k = input("Enter string and max combination size (e.g., HACK 2): ").split()
k = int(k)

# sorted string for lexicographic order
s = sorted(s)

# generate and print combinations of size 1 to k
print(f"Combinations up to size {k}:")
for size in range(1, k + 1):
    for combo in combinations(s, size):
        print(''.join(combo))