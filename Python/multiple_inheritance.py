class em:
    n="shafiul"
    def name(self):
        print(self.n)
class sh:
    m="islam"
    def dog(sel):
        print(sel.m)
class no:
    m=45
    @classmethod #if i use classmathod it does not take instant value
    def show(cl):
        print(cl.m)
# class mo:
#     n="mondol"
#     def job(self):
#         print(self.n)
# if i cannot update and show all of this we can use another class for print all of my value
class mo(em,sh):#its called inheritance if i change em class it will be update
    n="mondol"
    def job(self):
         print(self.n)
a=em()
b=mo()
c=no()
c.m=50# its a instant value of calss no. if i use classmathod it does not take instant value
c.show()
# c=sh()
a.name()
b.dog()
b.job()