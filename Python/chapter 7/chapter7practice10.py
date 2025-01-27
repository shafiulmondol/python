# write a program to multiplication table of a given number using for loop in revarse number
n=int(input("Enter your number: "))
for i in range(1,11):
    print(f"{n}X{11-i}={n*(11-i)}")