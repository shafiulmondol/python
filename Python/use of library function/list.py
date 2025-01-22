#in python every element is represented by index 
# for single element we can use indexing and for many element we can use slicing 
# syntex:- variale name[index] 
# syntex:-
list=[1,3,3+2j,'a',[2,3,4]]
print(list[4])
count=0
for i in list:
    print(i)
    count=count+1
print(count)
print(len(list))