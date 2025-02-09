'''a file contains a word multiple times. You need to write a program
 to which repless this word #### by updating the same file'''
word="name"
with open("d.txt") as f:
    c=f.read()
    cr=c.replace(word,"####")
with open("d.txt","w") as f:
    f.write(cr)