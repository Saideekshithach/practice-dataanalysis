
import numpy as np
import os
#n=int(input("enter number"))
try:
    #x=10/n
    #if n>=0:
        #print("positive number")
    #else:
        #raise ValueError("number is negative")
    #n.append(10)
    with open('sample.txt') as file:
        content=file.read()
        print(content)
        file.close()
    #file=open('sample.txt')
    #content=file.read()
    #print(content)
    #print(math.ceil(10.5))
    #x=[1,2,3,4,5]
    #y=np.array(x)
    #print(y*2)
   # print(x[10])
    #x=10+'a'
    #print(x)
    #print(n)
except PermissionError as e:
    print("permission denied",e)
#except OSError as e:
    #print("os error",e)
#except FileNotFoundError:
    #print("file not found")
#except ModuleNotFoundError:
    #print("module not found")
#except IndexError:
    #print("index out of range")
#except AttributeError:
    #print("object has no attribute")
#except TypeError:
    #print("object is not callable")
#except ZeroDivisionError as e:
    #print(e)
#except ValueError as e:
    #print(f"Invalid input:{e}")

#else:
    #print(f"Result:{x}")
finally:
    print("completed execution")