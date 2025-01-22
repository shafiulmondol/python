"""write a program to find whather a given number is prime or not"""
"""a=int(input("Enter your number : "))
c=1
for i in range(2,a):
    b=a%i
    if(b==0):
        c+=1
if(c==1):
    print(a," is a prime number ")
else:
    print(a, " is not a prime number ")"""
a=int(input("Enter your number : "))
for i in range(2,a):
    if(a%i)==0:
       print(a, " is not a prime number ")
       break
else:
    print(a," is a prime number ")

    