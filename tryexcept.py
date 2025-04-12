'''try:
    x=10/0
except ZeroDivisionError:
    print("Divide by zero")
finally:
    print('completed execution')
n=int(input("enter number:"))
try:
    x=10/n
except ZeroDivisionError as e:
    print(e)
finally:
    print('completed execution')
try:
    num=int(input("Enter a number"))
    result=10/num
except ValueError as e:
    print(f"Invalid input:{e}")
except ZeroDivisionError as e:
    print(f"cannot divided by zero")
except Exception as e:
    print("An unexpected")
else:
    print(f"Result:{result}")
finally:
    print(f"code executed successfully")
def checkage(age):
    if age<18:
        raise ValueError("Age must be 18")
    else:
        print("you are eligible")
try:
    checkage(10)
except ValueError as e:
    print("error",e)'''
class Noteligible(Exception):
    pass
def checkage(age):
    if age<18:
        raise Noteligible("age must be 18")
    else:
        print("you are eligible")
try:
    checkage(13)
except Noteligible as e:
    print("Error",e)
finally:
    print("executed successfully")
