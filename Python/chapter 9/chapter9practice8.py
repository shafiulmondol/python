'''write a program to make a coppy of a text file '''
with open("d.html") as f:
    coppy=f.read()
with open("dx.txt","w") as f:
    f.write(coppy)