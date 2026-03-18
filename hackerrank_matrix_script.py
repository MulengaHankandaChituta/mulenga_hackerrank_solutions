import re

n, m = map(int, input("Enter rows and columns (e.g. 7 3): ").split())

matrix = []

for i in range(n):
    while True:
        row = input(f"Enter row {i+1} (must be {m} characters): ")
        if len(row) == m:
            matrix.append(row)
            break
        else:
            print("Invalid input. Try again.")

decoded = ""

for col in range(m):
    for row in range(n):
        decoded += matrix[row][col]

decoded = re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', decoded)

print("\nDecoded message:")
print(decoded)
