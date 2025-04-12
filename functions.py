'''def greet():
    print("Hello,welcome")
greet()
def greet(name):
    print("Hello",name)
greet('sai')
def add(a,b):
    return a+b
result=add(5,3)
print("sum",result)
def greet(name="Guest"):
    print("Hello",name)
greet()
greet('Bob')'''
'''def get_details():
    name="Alice"
    age=25
    return name,age
n,a=get_details()
print("Name:",n,"Age",a)'''
def add_all(*numbers):
    return sum(numbers)#sum is the predefined function
print(add_all(1,2,3,4,5))
def info(**details):
    for key,value in details.items():
        for key,value in details.items():
            print(key,":",value)
info(name="Alice",age=25,city="New york")
