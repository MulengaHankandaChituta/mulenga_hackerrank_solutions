# Import the built-in HTMLParser class
from html.parser import HTMLParser

# Create a custom parser class by inheriting from HTMLParser
class MyHTMLParser(HTMLParser):

    # This method is called when a start tag like <div> is encountered
    def handle_starting(self, tag, attrs):

        # Print the start tag
        print("Start :", tag)

        # Loop through attributes inside the tag
        for name, value in attrs:
            # If attribute has no value (like: <option selected>)
            if value is None:
                value = "None"

            # Print attribute name and value in required format
            print("->", name, ">", value)

    # This method is called when an end tag like </div> is encountered
    def handle_endtag(self, tag):
        print("End    :", tag)

    # This method is called when an empty tag like <br /> is encountered
    def handle_startendtag(self, tag, attrs):
        # Print empty tag
        print("Empty :", tag)

        # Loop through attributes (if any)
        for name, value in attrs:
            if value is None:
                value = "None"
            print("->", name, ">", value)

# --------------- MAIN PROGRAM ----------------

# Read number of lines of HTML input
n = int(input())

# create an empty string tto store all HTML  lines
html_code = ""

# Read each line and append to html_code
for _ in range(n):
    html_code += input()

# Create a parser object
parser = HTMLParser()

# Feed the HTML content to the parser
parser.feed(html_code)

        
