import numpy as np
import time

x = np.random.rand(1000000)
y = np.random.rand(1000000)

tic = time.time()
c = np.dot(x,y)
toc = time.time()

print(c)
print("Vectorized version: " + str(1000*(toc-tic)) + " ms")

c = 0
tic = time.time()
for i in range(1000000):
    c+=x[i]*y[i]
toc = time.time()

print(c)
print("Foor loop: " + str(1000*(toc-tic)) + " ms")