import re

# Regex pattern for valid card structure
pattern = r'[456]\d{3}(-?\d{4}){3}$'

# Regex pattern for 4 cosecutive repeating digits
repeat_pattern = r'(\d)\1{3}'

n = int(input("Enter number of credit card numbers: "))

for i in range(n):
    card = input("Enter card number: ")

    # Remove hyphens before checking repeated digits
    digits = card.replace('-', '')

    if re.match(pattern, card) and not re.search(repeat_pattern, digits):
        print("Valid")
    else:
        print("Invalid")
