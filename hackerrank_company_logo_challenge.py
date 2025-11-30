from collections import Counter

# input from user
s =  input("Enter company name: ").strip()

# Count characters
count = Counter(s)

# sort by highest frequency, then alphabetical  order
sorted_chars = sorted(count.items(), key=lambda x: (-x[1], x[0]))

# Take top 3
top_three = sorted_chars[:3]

# print results
print("\nTop 3 most common characters:")
for char, freq in top_three:
    print(char, freq)
