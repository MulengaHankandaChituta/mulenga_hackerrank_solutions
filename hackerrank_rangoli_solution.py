# Alphabet rangoli solution
# from HackerRank

def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase

    lines = []

    for i in range(size):
        # left half descending letters
        left = '-'.join(alphabet[size-1:i:-1])

        # Middle letter
        middle = alphabet[i]

        # Right half ascending letters
        right = '-'.join(alphabet[i+1:size])

        # Combine parts and center with dashes
        line = '-'.join(filter(None, [left, middle, right]))
        lines.append(line.center(4*size-3, '-'))

    # Print the rangoli
    for line in lines[::-1] + lines[1:]:
        print(line)

if __name__ == '__main__':
    size = int(input("Enter the size of the rangoli: "))
    print_rangoli(size)