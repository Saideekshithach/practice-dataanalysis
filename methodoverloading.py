class result:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        else:
            return a*b

    
obj=result()
print(obj.add(9,9,7))
print(obj.add(4,5))