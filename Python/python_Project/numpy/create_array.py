import numpy as np
import keyboard

s = [1, 2, 3, 4]

a = np.array(s)
print("first array:", a)
print(a.ndim)
a2=np.array([[1,2,3,4],[1,2,3,4]])
print(a2)
print(a2.ndim)#it is two dimentional array
a3=np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(a3)
print(a3.ndim)# it is three dimentional array

# how many [] is present in this list this is the array dimention
a4=np.array([[[]]])
print(a4)
print(a4.ndim)
a5=np.array([[[[]]]])
print(a5)
print(a5.ndim)
an=np.array([],ndmin=10)# ndmin is get an input for user dimentional and friendly
print(an)
print(an.ndim)

d=[]# this part for the user input
for i in range (1,5):
    i=int(input('Enter array element: '))
    d.append(i)
print("second arrey is ",np.array(d))

