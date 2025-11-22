# program to count distinct country stamps

# ask for the number of stamps

n = int(input("How many stamps? "))

# create an empty set

countries = set()

# Read  each country name

for _ in range(n):
    country = input("Enter country name: ").strip()
    countries.add(country)

# print the number of unique countries
print("Total distinct country stamps:", len(countries))
