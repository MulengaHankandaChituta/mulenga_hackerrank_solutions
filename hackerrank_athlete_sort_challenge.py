# sorting a table based on the k-th column

# Read n (rows) and m (columns)
n, m = map(int, input("Enter n and m: ").split())

# read the table
arr = []
print("Enter the table rows:")
for _ in range(n):
    arr.append(list(map(int, input().split())))

# read the column index to sort by
k = int(input("Enter column index k: "))

# sort by the k-th column
arr.sort(key=lambda row: row[k])

# print the sorted table
print("\nSorted table:")
for row in arr:
    print(*row)
