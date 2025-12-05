# read the number of english subscribers

n_english = int(input())
english_subs = set(map(int, input().split()))

# read the number of french subscribers

n_french = int(input())
french_subs = set(map(int, input().split()))

# find intersection (students subscribed to both)

both = english_subs.intersection(french_subs)

# print results

print(len(both))
