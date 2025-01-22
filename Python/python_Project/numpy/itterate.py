import numpy
a=numpy.array([1,2,3])
for i in a:
    print(i)
print('------------------')
b=numpy.array([[1,2,3],[1,2,3]])
for i in b:
    for j in i:
        print(j)
print('------------------')
c=numpy.array([[[1,2,3],[2,4,5],[4,5,6]]])
for i in numpy.nditer(c):
    print(i)
for i,d in numpy.ndenumerate(c):# it create itteration and prints with index number
    print(i,d)