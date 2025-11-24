n = int(input().strip())

counts = {}
order = []

for _ in range(n):
    w = input().strip()
    if w not in counts:
        order.append(w)
        counts[w] = 1
    else:
        counts[w] += 1

print(len(order))
print(" ".join([str(counts[w]) for w in order]))
