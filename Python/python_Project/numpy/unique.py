import numpy
a=numpy.array([1,2,3,2,2,7,5,9,8,5,2,1,8,6,5,4])
b=numpy.unique(a,return_index=True,return_counts=True)
print(b)