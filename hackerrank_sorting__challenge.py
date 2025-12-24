# Program to sort a string based on custom rules:
# 1. Lowercase letters (sorted)
# 2. Uppercase letters (sorted)
# 3. Odd digits (sorted)
# 4. Even digits (sorted)

s = input("Enter a string: ")

lowercase = []
uppercase = []
odd_digits = []
even_digits = []

for ch in s:
    if ch.islower():
        lowercase.append(ch)
    elif ch.isupper():
        uppercase.append(ch)
    elif ch.isdigit():
        if int(ch) % 2 == 1:
            odd_digits.append(ch)
        else:
            even_digits.append(ch)

lowercase.sort()
uppercase.sort()
odd_digits.sort()
even_digits.sort()

sorted_string = "".join(lowercase + uppercase + odd_digits + even_digits)

print("Sorted result:", sorted_string)
