import numpy

a=numpy.array([1,2,3,4],ndmin=4)
print(numpy.shape(a))
a1=numpy.array([[1,2,3,4],[1,2,3,4]])
print(numpy.shape(a1))

print()
b=numpy.array([1,2,3,4,5,6,7,8])
b1=b.reshape(4,2)
print(b1)