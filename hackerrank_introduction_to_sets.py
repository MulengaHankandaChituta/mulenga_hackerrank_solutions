def average(array):
    # Convert list to a set to remove duplicates
    unique_elements = set(array)

    # calculate the average of the  unique elements
    avg = sum(unique_elements) / len(unique_elements)

    # Return the average rounded to 3 decimal places
    return round(avg, 3)

# Main function to read input and print the output
if __name__ == '__main__':
    # ask user for input
    n = int(input("Enter the number of elements: "))

    # Ask user to input elements seperated by spaces
    arr = list(map(int, input("Enter the elements seperated by spaces: ").split()))
    result = average(arr)
    print("The average of the unique elements is:", result)

    