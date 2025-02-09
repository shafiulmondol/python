"""Write a program to fill in a letter template given bellow with name and date
letter= dear <|name|>
you are selected!
<|date|>
"""
a=''' dear <|name|>
you are selected!
<|date|>'''
print(a.replace("<|name|>",input("Enter name:- ")).replace("<|date|>",input("Enter a date:- ")))