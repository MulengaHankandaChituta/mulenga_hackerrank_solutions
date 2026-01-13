# hackerRank: start() & end()
# This program finds all occurrences of a substring
# and prints their start and end indices (inclusive)

import re

# read input
string = input().strip()
substring = input().strip()

# lookahead pattern to allow overlapping matches
pattern = rf'(?=({substring}))'

# Find all matches
matches = list(re.finditer(pattern, string))

# if no matches are found
if not matches:
    print("(-1, -1)")
else:
    for match in matches:
        start_index = match.start(1)
        end_index = match.end(1) - 1 # inclusive index
        print((start_index, end_index))
