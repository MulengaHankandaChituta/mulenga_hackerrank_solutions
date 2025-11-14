import math

AB = float(input("Enter AB: "))
BC = float(input("Enter BC: "))

theta = math.degrees(math.atan(AB / BC))
theta_rounded = round(theta)

# Print actual degree symbol using Unicode escape
degree = "\u00b0"

print(str(theta_rounded) + degree)
