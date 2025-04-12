class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")
class Dog(Animal):
    def sound(self):
        return "woof!"
a=Animal("Generic Animal")#init method
d=Dog("Buddy")
print(a.name)#output:generic animal
print(d.name)#output:Buddy
print(d.sound())#





