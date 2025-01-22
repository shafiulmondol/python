# only function
n=int (input("how many students in your university: "))
def avg():
    a=int(input("Enter your number: "))
    b=int(input("Enter your number: "))
    c=int(input("Enter your number: "))
    aver=(a+b+c)/3
    print(aver)
for i in range(1,n): # for repeted this function i use for loop
    avg()# here i called the function avg
def sum(a,end):
    print("good day,",a)
    print(end)
sum("shafiul","mondol")

