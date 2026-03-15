import xml.etree.ElementTree as etree

maxdepth = 0

def depth(elem, level):
    global maxdepth
    level += 1
    maxdepth = max(maxdepth, level)
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""

    for i in range(n):
        xml += input()

    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()

    depth(root, -1)

    print(maxdepth)
    
