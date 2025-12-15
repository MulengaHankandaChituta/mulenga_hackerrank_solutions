# Read set A

A = set(map(int, input().split()))

# Read number of other sets
n = int(input())

# Check if  A is a strict superset of all other sets
for _ in range(n):
    B = set(map(int, input().split()))
    if not A > B: # strict superset check
        print(False)
        break
else:
    print(True)
