import cmath

# ask the user to enter a complex number
user_input = input("Enter a complex number (e.g, 1+2j): ")

# convert input string to a complex number
z = complex(user_input)

# calculate modulus (r) and phase angle (phi)
r = abs(z)
phi = cmath.phase(z)

# print the results
print("Modulus (r):", r)
print("Phase angle (phi in radians):", phi)