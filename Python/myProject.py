'''a file contains a word multiple times. You need to write a program
 to which repless this word to uppercase this word by updating the same file'''
story=input("Enter your story: ")
b=input("Enter your word that you are finding: ")
with open("story.txt","w") as g:
    g.write(story)
with open("story.txt","r") as f:
    d=f.read()
    dr=d.replace(b,b.upper())
with open("story.txt","w") as h:
    h.write(dr)