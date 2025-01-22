"""write a program to find out a student is pass or fail, if it require 40% 
 and at least 33% in each subject to pass. Assume 3 subject and take marks
   as an input from user"""
a={}
b=int(input("enter your bangla subject marks: "))

e=int(input("enter your english subject marks: "))

m=int(input("enter your math subject marks: "))

t=(100*(b+e+m))/300
if(t>=40 and b>=33 and e>=33 and m>=33):
    print("congratulation you pass in the exam",t)
else:
    print("you are failed try again",t)