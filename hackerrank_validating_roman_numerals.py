import re

# read input
s = input("Enter a roman numeral: ").strip()

# regular expression for a valid Roman numeral (1 to 3999)
regex_pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

# validate and print the result
if re.match(regex_pattern, s):
    print(True)
else:
    print(False)
