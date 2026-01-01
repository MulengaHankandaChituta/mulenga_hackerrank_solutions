cube = lambda x: x ** 3

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = list(map(cube, fibonacci(n)))
    print(result)
