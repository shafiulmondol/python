# the replace () methiod returns a coppy of string where all occurrence of a 
# sub-string replaced with another substring
# syntex: string.replace(old_value,new_value,count) 
# old_value= old substring you want to replace 
# new_value=new substring for old one
#count=optional argument.Number of time you want to replace
mess=input("Enter your message: ")
f=input("Enter your changing message: ")
c=input('enter your replace : ')
new=mess.replace(f,c)
print(new)