import numpy
a=numpy.matrix([[1,2],[4,5]])
print(a)
print('---------------------------')
print(numpy.transpose(a))
print('---------------------------')
print(numpy.swapaxes(a,0,1))
print('---------------------------')
print(numpy.linalg.inv(a))# inverse matrix
print('---------------------------')
print(numpy.linalg.matrix_power(a,3))# power of matrix
print('---------------------------')
print(numpy.linalg.det(a))