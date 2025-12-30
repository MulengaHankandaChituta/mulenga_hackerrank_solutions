# hackerrank any or all challenge
n = int(input("Enter number of integers: "))
arr = list(map(int, input("Enter the integers: ").split()))

print(all(x > 0 for x in arr) and any(str(x) == str(x)[::-1] for x in arr))
