a={}# it is a empty dictionery
mark={
"shafiul":100,
"sohan":200,
"asha":100
}
print(mark["sohan"])# i can find any specific value for veriables

print(mark.items())# in my dictionery which items is storeing it will show

print(mark.keys())# which veriable are stored in my dectionery it will show like shafiul sohan

print(mark.values())# it will shows the veriable values which are stored in my dictionery

mark.update({"shafiul":99})# here we can update any value of my veriables that is pree declared in my dectionery

print(mark.get("shafiul2"))# it prints none
#print(mark["shafiul2"])# it prints error
b={20,30,40}# this is a set. A set can not repeted elements
e=set()# this is a enpty set

b.add(60)#here we can add any elements
print(b)

#b.clear()# its clear the set elements

c={30,40,50}
print(b.union(c))# it takes all value between this two set

print(b.intersection(c))# it takes common value between this two set


