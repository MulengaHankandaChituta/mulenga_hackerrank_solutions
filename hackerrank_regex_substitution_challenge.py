import re

n = int(input())

for _ in range(n):
    line = input()

    # replace && with 'and' only when surrounded with spaces
    line = re.sub(r'(?<= )(&&)(?= )', 'and', line)

    # replace || with 'or' only when surrounded by spaces
    line = re.sub(r'(?= )(\|\|)(?= )', 'or', line)

    print(line)
