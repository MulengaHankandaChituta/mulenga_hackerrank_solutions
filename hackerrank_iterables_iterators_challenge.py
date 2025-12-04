# program to check the probability that atleast
# one chosen index contains 'a'

import math

n = int(input().strip())    # length of the list
letters = input().split()   # list of n lowercase letters
k = int(input().strip())    # number of indices to be selected

m = letters.count('a')      # how many "a's" in the list

# if we cannot choose k indices from n-m non-'a' letters, then probability = 1
if k == 0 or m == 0:
    prob = 0.0
elif n - m < k:
    prob = 1.0
else:
    total = math.comb(n, k)
    without_a = math.comb(n - m, k)
    prob = 1 - (without_a / total)

print("{:.4f}".format(prob))
