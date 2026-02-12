# program to validate unique identification UID

def is_valid(uid):
    # Must be exactly 10 characters
    if len(uid) != 10:
        return "Invalid"

    # must conntain only alphanumeric characters
    if not uid.isalnum():
        return "Invalid"

    # No character shoul repeat
    if len(set(uid)) != 10:
           return "Invalid"

    # Count uppercase letters
    uppercase_count = 0
    for char in uid:
        if char.isupper():
            uppercase_count += 1

    if uppercase_count < 2:
        return "Invalid"

    # count digits
    digit_count = 0
    for char in uid:
        if char.isdigit():
            digit_count += 1

    if digit_count < 3:
        return "Invalid"

    return "Valid"

# main program
t = int(input("Enter number of test cases: "))

for i in range(t):
    uid = input("Enter UID: ")
    print(is_valid(uid))
