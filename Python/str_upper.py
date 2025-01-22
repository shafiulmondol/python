string1='my name is shafiul'
b=string1.upper()# it convert all tetter to uppercase
print(b)
string2='i am a student'
c=string2.swapcase()# it convart upper case to lowarcase and lowarcase to upper case
print(c)
string3='my father name is asraful'
d=string3.title() # it convert all word's first charecter to uppercase
print(d)
string4='my mother name is shohida begum'
e=string4.capitalize()# it converts first letter of the sentence to uppercase 
print(e)
string5='i have 5 family member in my family'
s=string5.casefold()
print(s)
a=string1.center(len(string1)+10,'*') 
#syntex:- string.center(width,fillchar)
# width:-length of the string with paddes charecters
# fillchar:- padding character.it is optional argument. default value is space
# this mathod alligns string to the center by filling paddings left and right of the string
print(a)
a=string1.zfill(len(string1)+3)
#this method returns a coppy of string with '0'charecter padded to the left.
#syntex:- string.zfill(width)
print(a)