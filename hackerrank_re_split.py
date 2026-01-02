import re

regex_pattern = r"[,.]"

input_str =  input().strip()
result = re.split(regex_pattern, input_str)

for item in result:
    print(item)
