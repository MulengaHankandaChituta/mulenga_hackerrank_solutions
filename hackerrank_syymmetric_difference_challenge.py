# hackerRank Symmetric Difference Challenge

# read the size of set A

m = int(input("Enter size of set A: "))
a = set(map(int, input("Enter elements of set A: ").split()))

# read the size of set B

n = int(input("Enter size of setB: "))
b = set(map(int, input("Enter elements of set B: ").split()))

result = a.symmetric_difference(b)



print("\nSymmetric Difference Output:")
for value in sorted(result):
    print(value)
