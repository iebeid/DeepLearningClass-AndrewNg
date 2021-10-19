import numpy as np
import time

a = np.random.randn(5)

print(a)

print(a.shape)

print(a.T)

print(np.dot(a,a.T))

a = np.random.randn(5,1)
print(a)

print(a.T)

print(np.dot(a,a.T))
assert(a.shape==(5,1))

a = np.random.randn(3,4)
b = np.random.randn(4,1)
c = a+b.T
print(c)
