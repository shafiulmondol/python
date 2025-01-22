#using while loop
string=input("Enter your string: ")
print("original: ", string)
length=len(string)
re_string=""
while length>0:
    re_string=re_string+string[length-1]
    length=length-1
print("whiler",re_string)
# using for loop
rev=''
for new in string:
    rev=new+rev
print('for: ',rev)
# using slicing
sc=string[::-1]
print("slicing: ",sc)