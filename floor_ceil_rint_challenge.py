import numpy

# Set the output format
numpy.set_printoptions(legacy='1.13')

# get input from the user
my_array = numpy.array(list(map(float, input("Enter numbers separated by spaces: ").split())))

# print floor, ceil, and rounded values
print("Floor:")
print(numpy.floor(my_array))

print("Ceil:")
print(numpy.ceil(my_array))

print("Rint:")
print(numpy.rint(my_array))
