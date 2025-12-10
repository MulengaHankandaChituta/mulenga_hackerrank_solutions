# read initial set A

n = int(input())
A = set(map(int, input().split()))

# number of other sets
N = int(input())

for _ in range(N):
    # read the operation and length (length is not needed)
    op, length = input().split()
    other_set = set(map(int, input().split()))

    # perform mutation using getattr
    getattr(A, op)(other_set)

# Print the sum of elements in A
print(sum(A))
