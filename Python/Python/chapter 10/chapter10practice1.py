"""creat a class programer for storing information of few programers 
working at microsoft"""
class programer:
    company="microsoft"
    def __init__(self,name, salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
p=programer(input("Enter name: "),input("Enter salary: "),input("Enter pin: "))
print(p.name,p.salary,p.pin,p.company)
