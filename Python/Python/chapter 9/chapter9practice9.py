'''write a program to find out whater a file is identical and matches
 the content of another file'''
with open("d.html") as a:
    b=a.read()
with open("dx.txt") as a:
    c=a.read()
if(b==c):
    print("yes matches")
else:
    print("not matches")