import array
fruits=array.array('u',"applebananacherry","hello")
for fruit in fruits:
    print(fruit)

numbers=array.array('i',[1,2,3,4,5])
length=len(numbers)
print(length)
numbers_sorted=array.array('i',[1,5,4,2,3])
print(sorted(numbers_sorted))
