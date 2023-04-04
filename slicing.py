import numpy as np
#1d array slicing
s=np.array([1,2,3,4,2,6])
print(s)
print(s[::-1])
print(s[2:6:2])
#2d arrray slicing
a=np.array([[1,2,3],[4,5,6]])
print(a)
print(a[::,1::])
print(a[::,0::2])
print(a[::,2::])
#3d array slicing
au=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[2,3,4],[6,3,4],[6,8,9]]])
print(au)
print(au[1::,::,1::])
print(au[::,::,0:1:])

