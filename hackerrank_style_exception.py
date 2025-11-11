# HackerRank-style exception handling challenge

t = int(input())

for i in range(t):
    a_b = input().split()
    try:
        a, b = a_b[0], a_b[1]
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
