from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    blocks = deque(map(int, input().split()))

    possible = True
    last = float('inf')

    while blocks:
        left = blocks[0]
        right = blocks[-1]

        # choose the larger end first
        if max(left, right) <= last:
            if left >= right:
                last = left
                blocks.popleft()
            else:
                last = right
                blocks.pop()

        # if larger doesn't fit, try the smaller
        elif min(left, right) <= last:
            if left <= right:
                last = left
                blocks.popleft()
            else:
                last = right
                blocks.pop()
        else:
            possible = False
            break

    print("Yes" if possible else "No")
