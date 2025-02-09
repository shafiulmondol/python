'''write a python function which converts inches to cms'''
def inc(n):
    if(n==1):
        return 2.54
    return n*2.54
n=(float(input("Enter your value of inches: ")))
print("your cms value is: ",inc(n))