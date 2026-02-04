# import the built-in HTML parser
from html.parser import HTMLParser

# create a custom parser class
class MyHTMLParser(HTMLParser):

    # This method runs whenever an opening tag is found
    def handle_starttag(self, tag, attrs):
        # Print the tag name
        print(tag)

        # If the tag has attributes, print them
        for attribute in attrs:
            attr_name = attribute[0] # attribute name
            attr_value = attribute[1] # attribute value

            print("->", attr_name, ">", attr_value)

# read the number of lines
n = int(input("Enter number of lines: "))

# store full HTML content
html_code = ""

# read each line of HTML
for i in range(n):
    line = input()
    html_code += line + "\n"

# create parser object
parser = MyHTMLParser()

# feed the HTML content to parser
parser.feed(html_code)
