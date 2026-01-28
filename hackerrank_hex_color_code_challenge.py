import re # Import regex model

# read number of lines of CSS code

n = int(input())

# regex pattern for valid HEX color codes:
# - starts with #
# - followed by exactly 3 or 6 hex digits

hex_pattern = re.compile(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?')

# process each line of CSS

for _ in range(n):
    line = input()

    # Find ALL hex-like patterns in the current line

    for match in hex_pattern.finditer(line):

        # IMPORTANT RULE:
        # A valid color code must appear AFTER a colon (:)
        # This automatically excludes selectors like "#BED"

        if ':' in line[:match.start()]:
            print(match.group())
