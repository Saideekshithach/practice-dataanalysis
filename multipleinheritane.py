class parent:
    name="sai"
    def func2(self):
        print("this is parent class")
class parent2:
    name1="deekshi"
    def func2(self):
        print("this is parent2 class")
class son(parent,parent2):
    def func3(self):
        print("this is child class")
obj=son()
print(obj.name)
print(obj.name1)
obj.func2()
obj.func3()



