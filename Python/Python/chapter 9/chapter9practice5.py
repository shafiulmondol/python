'''repet program 4 for a list to such word to be consored'''
word=["name","shafiul","mondol"]
with open("d.txt") as f:
    c=f.read()
for w in word:
    c=c.replace(w,"####")
with open("d.txt","w") as f:
    f.write(c)