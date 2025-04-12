import os
'''if os.path.exists("test.txt"):
    with open('test.txt','r') as file:
        content=file.read()
        print(content)
else:
    print("file doesnot exist")
try:
    with open("test.txt",'r') as file:
        data=file.read()
    with open('test.txt','w') as filewrite:
        filewrite.write(data)
    print('file copied successfully')
except FileNotFoundError as e:
    print("input or output operation file")
except IOError as e:
    print("I/O exception",e)
except Exception as e:
    print("An unexpected error")'''
#f=open('example.txt','x')
#os.remove('example.txt')
#os.mkdir("myfolder")
os.rmdir("myfolder")
