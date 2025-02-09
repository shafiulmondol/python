'''add a static mathod in problem 2, to greet the user with hello.'''
class calculator:
    def __init__(self,n):
        self.n=n
    def squre(self):
        print(self.n**2)
    def cube(self):
        print(self.n**3)
    def squreroot(self):
        print(self.n**1/2)
    @staticmethod
    def hello():
        print("hellow there")
a=calculator(int(input("enter your numbr: ")))
a.hello()
a.squre()
a.cube()
a.squreroot()