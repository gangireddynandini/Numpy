import numpy as np
#1d indexing
a=np.array([1,2,3,4,5,6,7])
print(a)
n=[0,3,5]
ind=np.array(n)
print(a[ind])
#2d indexing
j=np.array([[1,2,3,8],[5,6,7,2],[2,3,4,6],[9,9,4,7]])
print(j)
print(j[1::,2::])
#accessing the diagonal elements
print(j[0,0],j[1,1],j[2,2],j[3,3])
print(j[[2,2],[3,2]])
#m3d indexing
a=np.array([[[2,3,4],[3,4,5],[9,6,3]],[[4,3,8],[3,6,2],[2,8,5]]])
print(a)
print(a[1,1,1],a[0,2,2])
print(a[0,1::,1::])
p=a[[0,1],[1,0],[2,0]]
print(p)