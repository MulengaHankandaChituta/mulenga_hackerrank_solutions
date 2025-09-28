# substring_counter.py
# Simple program to count occurences of a substring in a string
# this code is ready to be run in IDLE or as a script

def count_substring(string, sub_string):
    """Count the number of ooccurences of sub_string in string (allowing overlaps)"""
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    # prompt user for input
    string = input("Enter the main string: ").strip()
    sub_string = input("Enter the substring: ").strip()

    # print the result
    result = count_substring(string, sub_string)
    print(f"Occurrences of '{sub_string}' in '{string}': {result}")
