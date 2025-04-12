import numpy as np
a=input().split()
print(a)
print("".join(a))
b=input().split()
result=False
if "".join(a)== "".join(b):
    result=True
print(1 if result else 0)