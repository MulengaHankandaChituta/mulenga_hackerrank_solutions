# HackerRank Group().Groups() & Groupdict() challenge
# read the input string
s = input("Enter some input: ").strip()

# Flag to check if we found a repeating alphanumeric character
found = False

# Loop through the string, stopping at the second last character
for i in range(len(s) - 1):
    # Check if the current character is alphanumeric
    # and if it is the same as the next character
    if s[i].isalnum() and s[i] == s[i + 1]:
        # Print the first rrepeating alphanumeric character
        print(s[i])
        found = True
        break # Stop after finding the first occurrence

# If no reppeating alphanumeric character was found
if not found:
    print(-1)
