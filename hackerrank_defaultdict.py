"""
Program: defaultDict Example - Group Word Matching
Author: Mulenga Chituta
Description:
This Python program demonstrates the use of the defaultdict container
from the collections module. It reads two groups of words, Group A and Group B.

- Group A contains 'n words, which may repeat.
- Group B contains 'm' words that we will check against Group A.

For each word in Group B, the program prints the 1-based indices of all
occurences of that word in Group A. If a word from Group B does not appear
in Group A, the program prints -1.

This aproach uses defaultdict(list) to automatically handle new keys and
store multiple positions of the same word efficiently.

Example:
Input:
5 2
a
a
b
a
b
a
b

Output:
1 2 4
3 5
"""

from collections import defaultdict

# read two integers n and m
n, m = map(int, input().split())

# Create a defaultdict to store positions from Group A
group_a = defaultdict(list)

# Read words for Group A and store their positions
for i in range(1, n + 1):
    word = input().strip()
    group_a[word].append(i)

# read words for Group B and check if they appear in Group A
for _ in range(m):
    word = input().strip()
    if word in group_a:
        print(' '.join(map(str, group_a[word])))
    else:
        print(-1)
            
