class father():
    def func1(self):
        self.name="sai"
        self.age=22
        print(f"name is {self.name} and age is {self.age}")
class mother(father):
    def func2(self):
        self.name="deekshi"
        self.age=23
        print(f"name is {self.name} and age is {self.age}")
class child(mother):
    def func3(self):
        self.name="geetha"
        self.age=45
        print(f"name is {self.name} and age is {self.age}")
obj=child()
obj.func1()
obj.func2()
obj.func3()
