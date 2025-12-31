import re

def is_float_number(s):
    pattern = r'^[+-]?(\d+\.\d+|\.\d+)$'
    return bool(re.match(pattern, s))

def main():
    t  = int(input("Enter number of test cases: "))
    for _ in range(t):
        value = input("Enter value: ")
        print(is_float_number(value))

if __name__ == "__main__":
    main()
