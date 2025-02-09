"""write a program to find the sum of first n natural numbers using while loop"""
n=int (input("Enter your number: "))
i=0
s=0
while(i<=n):
    s=s+i
    i+=1

print(s)