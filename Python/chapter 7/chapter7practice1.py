# write a program to multiplication table of a given number using for loop
a=int(input("Enter your number : "))
for i in range(1,11):
    b=a*i
    print(a, "*", i, "=",b)