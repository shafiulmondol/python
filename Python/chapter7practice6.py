"""write a program to find the factorial of a given number by using for loops"""
a=int (input("Enter your number: "))
b=1
for i in range(1,a+1):
    b=i*b
print(b)
