# read K (number of lists) and M (modulo value)

K, M = map(int, input().split())

# read all K lists
lists = []
for _ in range(K):
    line = list(map(int, input().split()))
    n = line[0] # first number is the count of elements
    elements = line[1:n+1] # get the actual elements
    lists.append(elements)

# initialization with squares of first list elements (mod M)
possible_sums = set()
for num in lists[0]:
    possible_sums.add((num * num) % M)

# Process each remaining list
for i in range(1, K):
    new_sums = set()
    for num in lists[i]:
        square = (num * num) % M
        # combine current element with all previous sums
        for prev_sum in possible_sums:
            new_sum = (prev_sum + square) % M
            new_sums.add(new_sum)
    possible_sums = new_sums

# output the maximum possible value
print(max(possible_sums))
