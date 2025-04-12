class parent:
    def __init__(self,age):
        self.age=age
    def func1(self):
        print("this is parent class")
class child(parent):
    def func2(self):
        print("this is child class")
class child2(parent):
    def func3(parent):
        print("this is child2 class")
obj=child(22)
obj.func1()
obj.func2()
print(obj.age)



