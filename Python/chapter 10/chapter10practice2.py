"""write a class calculator  capable of finding square, cube and squre root of a number"""
class calculator:
#     number=float(input("Enter your number: "))
#     squre=number**2
#     cube=number**3
#     squreroot=number**1/2
# ans=calculator()
# print(ans.number,ans.squre,ans.cube,ans.squreroot)
    def __init__(self,n):
        self.n=n
    def squre(self):
        print(self.n**2)
    def cube(self):
        print(self.n**3)
    def squreroot(self):
        print(self.n**1/2)
a=calculator(int(input("enter your numbr: ")))
a.squre()
a.cube()
a.squreroot()