'''class Dog:
    sound="bark"
dog1=Dog()
print(dog1.sound)

class cat:
    def cat1(self):
        print("cat1")
ca=cat()
print(ca.cat1())'''
class Dog:
    species="canine"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old."
#dog1=Dog()
dog1=Dog("Buddy",3)
dog2=Dog("Charlie",4)
print(dog1)
print(dog2)
#print(dog1.name)
#print(dog1.age)
dog1.name="Max"
Dog.species="feline"
dog1.species="carrot"
print(dog1.name)
print(Dog.species)
print(dog1.species)