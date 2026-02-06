import xml.etree.ElementTree as etree

def get_attr_number(node):
    # Count attributes of current node
    score = len(node.attrib)

    # recursively count attributes of children
    for child in node:
        score += get_attr_number(child)

    return score

# ----- Main Program ------
n = int(input("Enter number of lines: "))

xml = ""
print("Paste the XML lines below:")

for _ in range(n):
    xml += input() + "\n"

root = etree.fromstring(xml)

print("Total Attribute Score:", get_attr_number(root))
