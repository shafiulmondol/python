'''write a function program to print the following pattern
***
**
*
n=3
'''
def p(n):
    if(n==0):
        print("")
        return 
    print("* "*n)
    p(n-1)
p(int(input("Enter your number: ")))