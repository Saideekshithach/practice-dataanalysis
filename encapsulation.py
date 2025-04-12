class private():
    def __init__(self):
        self.__salary=5000
        self._dept="cse"
    def salary(self):
        return self.__salary
obj=private()
print(obj.salary())
print(obj._dept)
print(obj.__salary())
