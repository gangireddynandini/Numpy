import numpy as np
l1=(1,2,2,34,5,5)
u=np.array(l1)
y=u.reshape(2,3)
print(y)
print(y.shape)
print(y.ndim)
print(y.dtype)
print(y,type(y))
l2={1:"nandu",2:"madhu",3:'aadya'}
h=np.array(l2)
print(h,type(h))