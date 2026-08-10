import numpy as np

# Enter polynomial coefficients

coefficients = list(map(float, input("Enter coefficients: ").split()))

# Enter the value of x
x = float(input("Enter x: "))

# Evaluate the polynomial

result = np.polyval(coefficients, x)

print("Result:", result)
