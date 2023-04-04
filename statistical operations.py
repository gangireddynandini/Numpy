import numpy as np
import statistics as s
l1=[[1,8,4],[8,3,0],[2,7,0]]
h=np.array(l1)
b=np.amax(h,axis=0)
print(b)
b=np.amax(h,axis=1)
print(b)
b=np.amin(h,axis=0)
print(b)
b=np.amin(h,axis=1)
print(b)
b=np.mean(h,axis=0)
print(b)
b=np.var(h,axis=0)
print(b)
b=np.std(h,axis=0)
print(b)
b=np.median(h,axis=0)
print(b)
a=[6,7,0,6,3,2,6]
p=s.mode(a)
print(p)