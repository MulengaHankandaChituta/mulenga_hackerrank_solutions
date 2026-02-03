# HTML Parser - Part 2 (Comments and Data)

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    # This method is called when a comment is encountered
    def handle_comment(self, data):

        # If the comment contains a newline, it is multi-line
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    # This method is called when text data is encountered
    def handle_data(self, data):

        # Do not print empty newline data
        if data != '\n':
            print(">>> Data")
            print(data)

# Read number of lines
n = int(input())

# Read HTML lines
html = ""
for _ in range(n):
    html += input()
    html += "\n"

# Create parsser object
parser = MyHTMLParser()

# feed HTML content to parser
parser.feed(html)

# Close parser
parser.close()
