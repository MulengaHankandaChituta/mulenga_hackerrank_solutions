import numpy

A = numpy.array(list(map(int, input("Enter array A: ").split())))
B = numpy.array(list(map(int, input("Enter array B: ").split())))

print("\nInner product:")
print(numpy.inner(A, B))

print("\nOuter product:")
print(numpy.outer(A, B))
