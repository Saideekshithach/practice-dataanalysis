import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[2,0],[1,2]])
print(np.dot(a,b))
print(np.transpose(a))
print(np.linalg.inv(a))
print(a[0,1])
print(a[:,1])
print(a[1])
