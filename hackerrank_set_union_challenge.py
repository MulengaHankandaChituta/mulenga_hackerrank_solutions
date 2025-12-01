# read number of english subscribers

n = int(input())
english = set(map(int, input().split()))

# read number of french subscribers

b = int(input())
french = set(map(int, input().split()))

# union gives students with at least one subscription

result = english.union(french)

#  print total number

print(len(result))
