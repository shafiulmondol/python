import numpy
a=numpy.array([1,2,3,2,1,2,3,4,3,2,2,3,1,])
print(numpy.where(a==2))
a=numpy.array([1,2,3,2,1,2,3,4,3,2,2,3,1,])
print(numpy.where((a%2)==0))
a=numpy.array([1,2,3,2,1,2,3,4,3,2,2,3,1,])
print(numpy.searchsorted(a,2,side='left'))
p=(numpy.searchsorted(a,3,side='left')) # that is insert an element with a sequence wise
print(p)