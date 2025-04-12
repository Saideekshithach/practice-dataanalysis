#lambda function
'''s1="Hello good morning"
s2=lambda func:func.upper()
print(s2(s1))

n=lambda x:"positive" if x>0 else "negative" if x<0 else "zero"
print(n(5))
print(n(-4))
print(n(0))


sq=lambda x:x**2
print(sq(5))

def sqdef(x):
    return x**2
print(sqdef(5))
li=[lambda arg=x:arg*10 for x in range(1,5)]
for i in li:
    print(i())

check=lambda x:"Even" if x %2==0 else "odd"
print(check(10))
print(check(5))

calc=lambda x,y:(x+y,x*y)
res=calc(3,4)
print(res)'''

n=[1,2,3,4,5]
even=filter(lambda x:x%2==0,n)
print(list(even))
print(even)



