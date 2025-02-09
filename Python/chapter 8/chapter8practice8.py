'''write a puthon function to print multiplication table of a given number'''

def mul(n):
    for i in range(1,11):
        print(f"{i} X {n} ={n*i}")
mul(int(input("Enter your number: ")))
