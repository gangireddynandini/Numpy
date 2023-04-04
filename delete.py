import numpy as np
e=np.array([3,4,5,6,7,7,9,2,3,7])
print(np.delete(e,2))

print(np.delete(e,[2,4]))
#2d array
e=np.array([[3,4,5,6,7],[7,9,2,3,7]])
print(e)
print(np.delete(e,1,axis=0))
print(np.delete(e,[2,3],axis=1))


