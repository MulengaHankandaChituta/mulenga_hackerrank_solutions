import re # Import the regular expression module

# read the number of mobile numbers to check

n = int(input())

# loop through each input mobile number

for _ in range(n):
    mobile = input("Enter the mobile number: ").strip() # Read the mobile number and remove extra spaces

    # Check if the number
    # - starts with 7, 8, 9
    # - has exactly 10 digits
    if re.match(r'^[789]\d{9}', mobile):
        print("YES") # valid mobile number
    else:
        print("NO")
