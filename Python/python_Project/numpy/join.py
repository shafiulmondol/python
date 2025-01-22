import numpy
a=numpy.array([1,2,3,4])
b=numpy.array([5,6,7,8])
c=numpy.concatenate((a,b))
print(c)
print('--------------------')
a1=numpy.array([[1,2,3,4]])
b1=numpy.array([[5,6,7,8]])
c1=numpy.concatenate((a1,b1),axis=1)# 1 means row wise and 0 means column wise
print(c1)
print('--------------------')
a2=numpy.array([[1,2,3,4]])
b2=numpy.array([[5,6,7,8]])
c2=numpy.concatenate((a2,b2),axis=0)# 1 means row wise and 0 means column wise
print(c2)
print('--------------------')
a3=numpy.array([[1,2,3,4]])
b3=numpy.array([[5,6,7,8]])
c3=numpy.stack((a3,b3),axis=0)# 1 means row wise and 0 means column wise
print(c3)
print('--------------------')
a4=numpy.array([[1,2,3,4]])
b4=numpy.array([[5,6,7,8]])
c4=numpy.dstack((a4,b4))# 1 means row wise and 0 means height wise
print('height')
print(c4)
print('--------------------')
a5=numpy.array([[1,2,3,4]])
b5=numpy.array([[5,6,7,8]])
c5=numpy.hstack((a5,b5))# that works on to row
print('row')
print(c4)
print('--------------------')
a6=numpy.array([[1,2,3,4]])
b6=numpy.array([[5,6,7,8]])
c6=numpy.vstack((a6,b6))# that works on to column
print('colum')
print(c4)