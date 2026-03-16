# function to standardize mobile numbers

# Decorator function
def wrapper(f):
    # This inner function receives the list of numbers
    def fun(l):
        formatted_numbers = [] # list to store formatted phone numbers

        # loop through each number in the list
        for num in l:
            num = str(num)[-10:] # take only the last 10 digits (removes 0, 91, etc.)

            # Format the number into required format
            formatted = "+91 " + num[:5] + " " + num[5:]

            # Add the formatted number to the list
            formatted_numbers.append(formatted)

        # sort the numbers and pass them to the original function
        f(sorted(formatted_numbers))

    # return the inner function
    return fun

# Apply the decorator to this function
@wrapper
def sort_phone(l):
    # print each phone number on a new line
    for number in l:
        print(number)

# ----- Input Section ----

# ask the user for how many phone numbers they will enter
n = int(input("Enter number of phone numbers: "))

numbers = [] # list to store input phone numbers

# loop to collect the phone numbers
for i in range(n):
    num = input("Enter phone number: ")
    numbers.append(num) # add number to the list

# call the function to format, sort, and print the numbers
sort_phone(numbers)

    
