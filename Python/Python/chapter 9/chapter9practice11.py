'''write a program to rename a file'''
with open("dx.txt") as f:
    a= f.read()
with open("new.txt","w") as f:
    f.write(a)