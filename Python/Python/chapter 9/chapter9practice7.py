'''write a program to find out the line where pythhon is present for quiz 6'''
line=1
g=input("Enter your file name: ")
word=input("Enter your word that you are finding: ")
c=1
with open(g) as f:
        y=f.readlines()
for lines in y:
    if(word in lines):
        print(line,"\n")
        c+=1
    line+=1
else:
    if(c==1):
        print("not found")
