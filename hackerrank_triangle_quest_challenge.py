# This program prints a palindromic number triangle of size n.
# It uses only mathematics (no strings), as required by the HackerRank challenge.
# The expression ((10**i - 1) // 9) generates a number made of i ones (1, 11, 111...).
# Squaring that number creates the palindromic pattern (1, 121, 12321...).

for i in range(1, int(input("Enter size: ")) + 1):
    print(((10**i - 1) // 9) ** 2)
