def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input("Enter a string: ")
    result = swap_case(s)
    print("Swapped case:", result)
