"""HackerRank challenge split and join"""

def split_and_join(line):
    # split on spaces and join with hyphens
    return "_".join(line.split(" "))

if __name__ == '__main__':
    line = input("Enter a string: ")
    result = split_and_join(line)
    print(result)