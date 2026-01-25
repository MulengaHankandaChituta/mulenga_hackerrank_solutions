import re                 # Import regex module for pattern matching
import email.utils        # Import email utilities to parse name and email

# Read the number of email entries
n = int(input())

# Regular expression for a valid email address
# 1. Starts with a letter
# 2. Followed by letters, digits, dot, underscore, or dash
# 3. Contains @
# 4. Domain contains only letters
# 5. Extension contains 1 to 3 letters
pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

# Loop through each input line
for _ in range(n):
    line = input()  # Read the full line (e.g. NAME <email>)
    
    # Extract name and email address from the line
    name, addr = email.utils.parseaddr(line)
    
    # Check if the extracted email matches the pattern exactly
    if re.fullmatch(pattern, addr):
        # Print the name and email in the required format
        print(email.utils.formataddr((name, addr)))
