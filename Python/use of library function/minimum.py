#to find minimum in list or tuple or set or another activities
#syntex=min(iterable,key,default)
#iterable: an iterable such as list. 
# key(optional): basis for comparision 
# defaut: default value is given iterable is enpty
list=[3,2,4,5,3,7,5,12]
print(min(list))
list1=['shafiul','mondol','sohan','asha']
print(min(list1))# it consider asci value of charecter not length of element
print(min(list1,key=len))# it consider length of element not asci value of charecter
n=list[0]
for m in list:
    if m>n:
        n=m
    
    else:
        continue
print('max',n)
n=list[0]
for m in list:
    if m<n:
        n=m
    
    else:
        continue
print('min',n)