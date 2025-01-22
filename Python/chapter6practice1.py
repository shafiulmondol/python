"""
write a programe to find gratest number from 4 numbers enterd by the user
"""
a=input("Enter your first number: ")
b=input("Enter your second number: ")
c=input("Enter your third number: ") 
d=input("Enter your fourth number: ")
if(a>b and a>c and a>d):
    print(a, "is greatest")
elif(b>c and b>d and b>a):
    print(b, "is greatest")
elif(c>a and c>b and c>d):
    print(c, "is greatest")
else:
    print(d, "is  greatest")                 