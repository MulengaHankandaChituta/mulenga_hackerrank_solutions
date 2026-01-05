from functools import reduce
from fractions import Fraction

def product(fracs):
    # Multiply all fractions using reduce
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

# IDLE execution starts here
if __name__ == '__main__':
    n = int(input("Enter number of fractions: ")) # number of fractions
    fracs = []

    for _ in range(n):
        num, den = map(int, input().split())
        fracs.append(Fraction(num, den))

    result = product(fracs)
    print(result[0], result[1])
