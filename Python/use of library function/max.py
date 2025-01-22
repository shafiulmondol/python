#to find maximum in list or tuple or set or another activities
#syntex=max(iterable,key,default)
#iterable: an iterable such as list. 
# key(optional): basis for comparision 
# defaut: default value is given iterable is enpty
list=[3,2,4,5,3,7,5,12]
print(max(list))
list1=['shafiul','mondol','sohan','asha']
print(max(list1))# it consider asci value of charecter not length of element
print(max(list1,key=len))# it consider length of element not asci value of charecter
