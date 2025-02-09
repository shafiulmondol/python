'''write a programe to convert celcious to farenheight temperature'''
a=input("what do you want: ")
if(a=="c to f"):
    c=float(input("Enter your celcious temperature:"))
else:
    s=float(input("Enter your farenteight temperature:"))
def change():
    f=(9*c/5)+32
    print(f , "is your farenheight temperature")
def ch():
    d=(5/9)*(s-32)
    print(d , "is your celcious temperature")
if(a==("c to f")):
    change()
else:
    ch()
