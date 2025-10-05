import textwrap

def wrap(string, max_width):
    """Wraps the input string into lines of of the given width."""
    return '\n'.join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    print("=== Text Wrap Challenge ===")
    string = input("Enter a strinng: ")
    max_width = int(input("Enter the width to wrap to: "))

    result = wrap(string, max_width)
    print("\nWrapped Text:\n")
    print(result)