a="shafiul"
#  0,1,2,3,4,5,6
#  -7,-6,-5,-4,-3,-2,-1 count index with revarce
b=["shafiul","orenge"]
c=[5,3,7,20,30,12,23]
print(len(a))
print(a[0:3])
print(a[-1:-4]) #maintain serial
print(a[-4:-1])
print(a[1:4])
print(a[:4])# blank means 0 index. same as a[0:4]
print(a[1:])# blank means lenth of string. same as a[1:7]
print(a[1:7])
print(a[1:7:2])#[start:end:gap]
print(a[1::2])# same as [1:7:2]. gap means lenth of the string
print(a.startswith("sha"))# startswith means which char start the string
print(a.startswith("asha"))# its false because asha is not starting char
print(a.endswith("fiul"))# endswith means which char end the string
print(a.startswith("asha"))# its false because asha is not ending char
print(a.capitalize()) # for capitalize the first char of the string ue can use capitalize

b.append(" shohan") # add any element in at the end ue can use append
print(b)

b.insert(2,"asha")
"""if we add any element in a list at any index we can use insert"""
print(b)

b.pop(1)
""" pop is delated this index values"""
print(b)

c.reverse()
"""for revarse any listing number ue can use revarse. for that this
 number will be started from end . not desinding"""
print(c)

c.sort() # for assending order ue can use sort
print(c)
