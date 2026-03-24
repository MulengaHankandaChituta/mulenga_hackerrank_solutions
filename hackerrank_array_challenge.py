import numpy as np

def array(arr):
    # Convert list to NumPy array of type float
    arr = np.array(arr, float)

    # Reverse the array
    return arr[::-1]

# Take input from user
arr = input("Enter space seperated numbers: ").strip().split(' ')

# call function and print result
result = array(arr)
print(result)
