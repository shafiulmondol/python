"""write a program to print the following pattern for n=3
  *
 ***
*****
"""
n=int(input("Enter your number: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("\n")