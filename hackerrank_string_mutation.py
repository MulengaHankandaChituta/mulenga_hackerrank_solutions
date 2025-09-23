"""HackerRank string mutation challenge"""
def  mutate_string(string, position, character):
    # replace character at the given index using slicing
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input("Enter a string: ")
    i, c = input("Enter the position and character: ").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)