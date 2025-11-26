# HackerRank set operations challenge
# It can be run directly in IDLE

# Sample input
n = 9
s = set([1,2,3,4,5,6,7,8,9])
commands = [
    "pop",
    "remove 9",
    "discard 9",
    "discard 8",
    "remove 7",
    "pop",
    "discard 6",
    "remove 5",
    "pop",
    "discard 5"
]

print("Initial set:", s)
print()

# process each command
for cmd in commands:
    command = cmd.split()

    if command[0] == 'pop':
        removed = s.pop()
        print(f"pop -> removed {removed}, set: {s}")
    elif command[0] == 'remove':
        value = int(command[1])
        s.remove(value)
        print(f"remove {value} -> set: {s}")
    elif command[0] == 'discard':
        value = int(command[1])
        s.discard(value)
        print(f"discard {value} -> set: {s}")

print()
print("Final set:", s)
print("Sum of remaining elements:", sum(s))
