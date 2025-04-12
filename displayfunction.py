def details():
    name=input()
    age=int(input())
    gender=input()
    return name,age,gender
def display():
    n,a,g=details()
    print("name",n,"age",a,"gender",g)
display()
