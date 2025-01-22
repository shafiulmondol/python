'''write a program to using function to find greatest of three numbers'''
a=int (input("Enter your number:"))
b=int (input("Enter your number:"))
c=int (input("Enter your number:"))

def great():
    if(a>b and a>c):
     print(a , "is greatest")
    elif(b>a and b>c):
       print(b , "is greatest")
    else:
       print(c , "is greatest")

great()