from itertools import groupby

def compress_string(s):
    result = []
    for key, group in groupby(s):
        count =  len(list(group))
        result.append(f"({count}, {key})")
    return " ".join(result)

if __name__ == "__main__":
    s = input("Enter a string of digits: ").strip()
    print(compress_string(s))
