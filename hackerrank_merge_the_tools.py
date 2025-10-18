def merge_the_tools(string, k):
    # loop through the string in steps of k
    for i in  range(0, len(string), k):
        # extract substring of length k
        substring = string[i:i+k]
        result = ""
        # remove duplicate characters while keeping order
        for char in substring:
            if char not in result:
                result += char
        # print the final processed result
        print(result)

if __name__ == '__main__':
    # Input string
    s = input("Enter the string: ").strip()
    # Input integer k
    k = int(input("Enter the value of k: "))
    # Call the function
    merge_the_tools(s, k)