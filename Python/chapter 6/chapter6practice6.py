"""write a program to calculate the grade of a student from his mark from the following sheme
90-100=Ex
80-90=A
70-80=B
60-70=C
50-60=D
<50=F"""
a=float(input("Enter your marks: "))
if(a>=90 and a<=100):
    print("your grade is Ex")
elif(a>=80 and a<90):
    print("your grade is A")
elif(a>=70 and a<80):
    print("your grade is B")
elif(a>=60 and a<70):
    print("your grade is C")
elif(a>=50 and a<60):
    print("your grade is D")
else:
    print("your grade is F")
