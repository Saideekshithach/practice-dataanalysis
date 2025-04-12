class public:
    def __init__(self,name,age,gender):
        self._name=name
        self.__age=age
        self.gender=gender
    def display(self):
        print(f"name is {self._name} is age is {self.__age}")
b=public("sai",22,'f')
print(b.display())
print(b._name)
print(b.gender)
print(b.__age)


