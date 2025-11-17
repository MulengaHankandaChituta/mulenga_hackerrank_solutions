# read n and m
n, m = map(int, input().split())

# read the array
arr = list(map(int, input().split()))

# read set A (liked values)
A = set(map(int, input().split()))

# read set B (disliked values)
B = set(map(int, input().split()))

happiness = 0

for x in arr:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1

print(happiness)
