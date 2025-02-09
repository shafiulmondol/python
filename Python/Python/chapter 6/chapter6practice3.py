"""a spam comment is defined as a lest consesting following keywords
"make a lot of money""bye now""subscribe" "click this"
"""
a="make a lot of money"
b="bye now""subscribe" 
c="click this"
d=input("Enter your message:\n")
e=d.find("   ")
if((a in d)or (b in d) or (c in d)):
    print("\nyour comment in spam\n")
if(e!=-1):
    print("your write message is: ",d.replace("   "," "))
