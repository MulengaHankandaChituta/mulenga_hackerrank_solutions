# HackerRank Lists Problem Solution
# Author: Mulenga Chituta

if __name__ == '__main__':
    N = int(input("Enter number of commands: "))  # number of commands
    my_list = []

    for _ in range(N):
        command = input("Enter command: ").split()
        operation = command[0]

        if operation == "insert":
            i, e = int(command[1]), int(command[2])
            my_list.insert(i, e)

        elif operation == "print":
            print(my_list)

        elif operation == "remove":
            e = int(command[1])
            if e in my_list:
                my_list.remove(e)

        elif operation == "append":
            e = int(command[1])
            my_list.append(e)

        elif operation == "sort":
            my_list.sort()

        elif operation == "pop":
            if my_list:
                my_list.pop()

        elif operation == "reverse":
            my_list.reverse()
