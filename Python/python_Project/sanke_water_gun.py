'''we will have played a snake water gun game in our childhood.
 If you haven't google the rules of this game and write a pthon program 
 capable of this game with the usser'''
# 1 for snake 
#-1 for water 
# 0 for gun
import random
c=random.choice([-1, 0, 1])
a=input("Enter your choice:\n snake for s,water for w and gun for g: " )
my={"s":1,"w":-1,"g":0}
s=my[a]# here i convert "user input" according to "my" dictionery 
myc={1:"sanke" ,-1:"water" ,0:"gun" }
mych=myc[s]# here i convert "s value" according to "myc" dictionery 
computer=myc[c]# here i convert "c's value" according to "myc" dictionery 
print("computer: ",computer)
print("you: ",mych)
if(c==s):
    print("----It's a drow----")
else:
    if(c==1 and s==-1):
        print("-----You lost!----")
    elif(c==1 and s==0):
        print("-----You win!----")
    elif(c==-1 and s==1):
        print("-----You win!----")
    elif(c==-1 and s==0):
        print("-----You lost!----")
    elif(c==0 and s==1):
        print("-----You lost!----")
    elif(c==0 and s==-1):
        print("-----You win!----")
    else:
        print("something wrong---------")