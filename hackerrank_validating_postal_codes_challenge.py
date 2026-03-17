import re # Import Python's regular expression module

# Read input (postal code) and remove any extra spaces
p = input().strip()

# Regex 1:
# ^  start of string
# [1-9] first digit must be 1-9 (no leading zero)
# [0-9]{5} exactly 5 more digits (total = 6 digits)
# $ end of string

regex_integer_in_range = r"^[1-9][0-9]{5}"

# regex 2:
# (?=...)  lookahead (allows overlapping matches)
# (\d)  capture any digit
# \d any digit in between
# \1  same digit again (backreference)
# This finds patterns like 121, 343, etc.

regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"

# checck if:
# 1. Postal code matches the required 6-digit format
# 2. Number of alternating repetitive digit pairs is less than 2

is_valid = (
    bool(re.match(regex_integer_in_range, p)) and
    len(re.findall(regex_alternating_repetitive_digit_pair, p)) < 2
)

# output result (True or false)
print(is_valid)
