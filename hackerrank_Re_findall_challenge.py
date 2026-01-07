import re # Import regular expressions module

# Read the input string and remove leading/trailing spaces
s = input().strip()

# Regex pattern explanation:
# (?<=[^aeiouAEIOU])  -> positive lookbehind: previous character must be a consonant
# ([aeiouAEIOU]{2,})  -> capture group: 2 or more vowels only
# (?=[^aeiouAEIOU])   -> positive lookahead: next character must be a consonant
pattern = r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])'

# find all matching vowel-only substrings
matches = re.findall(pattern, s)

# If at least one match is found
if matches:
    # print each matched substring on a new line
    for m in matches:
        print(m)
else:
    # If no matches are found, print -1
    print(-1)
