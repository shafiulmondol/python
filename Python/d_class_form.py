'''basic'''
class employee:
    name="shafiul"# This is an object attribute
    lan="py"# This is an Class attribute
    salary=12334# This is an Class attribute
    def my(self):# for indicating this function we use self or functon object. If we dont use we have an error
        print(f"language is {self.lan}. Salary is {self.salary}")
        print("good morning")
    @staticmethod # if we use this mathood we have no need to define object.
    def name():
        print("There have no need to define object")
shafiul=employee()
shafiul.my()
shafiul.name()