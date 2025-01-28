'''write a python function to remove a given word from a list and 
skip it at the same time'''
l=["shafiul","mondol","sohan","asha"]
def rem(l,word):
    for item in l:
        l.remove(word)
        return l
print(rem(l,input("Enter your word: ")))

def mo(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
        return n
print(mo(l,input("Enter your letter: ")))