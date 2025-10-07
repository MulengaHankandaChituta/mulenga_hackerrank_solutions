# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read input values
rows, cols = map(int, input().split())

# Top section
for i in range(1, rows, 2):
    print((".|." * i).center(cols, "-"))

# Middle line
print("WELCOME".center(cols, "-"))

# Bottom section
for i in range(rows - 2, 0, -2):
    print((".|." * i).center(cols, "-"))