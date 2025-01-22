class em:
    n="shafiul"
    def name(self):
        print(self.n)
# class mo:
#     n="mondol"
#     def job(self):
#         print(self.n)
# if i cannot update and show all of this we can use another class for print all of my value
class mo(em):#its called inheritance if i change em class it will be update
    n="mondol"
    def job(self):
         print(self.n)
a=em()
b=mo()
print(a.n,b.n)
a.name()
b.job()