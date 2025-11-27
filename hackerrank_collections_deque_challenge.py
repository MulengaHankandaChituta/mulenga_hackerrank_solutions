from collections import deque

def main():
    d = deque()
    n = int(input())

    for  _ in range(n):
        command = input.split()

        if command[0] == "append":
            d.append(command[1])
        elif command[0] == "appendleft":
            d.append(command[1])
        elif command[0] == "pop":
            if d:
                d.popleft()

    print(*d)

if __name__ == "__main___":
    main()
