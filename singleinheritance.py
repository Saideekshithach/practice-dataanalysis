class parent():
    name="sai"
    def func1(self):
        print("This is parent class")
class child(parent):
    name1="deekshi"
    def func2(self):
        print("This is child class")
obj=child()
obj.func1()
obj.func2()
print(obj.name)
print(obj.name1)