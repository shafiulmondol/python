'''creat a class with class attribute a; creat an object from it and set
 a directly using object a=0; does this class attribue'''
class sum:
    a=4
o=sum()
print(o.a)# prints the class attribute because instant attribute is not present
o.a=0 # instance attribute is set
print(o.a)#prints the instance attribute because instance attribute in present
print(sum.a)#prints the class attribute