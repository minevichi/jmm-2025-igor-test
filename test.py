from time import *

def myFun(i):
    s = 0
    for j in range(i):
        s += j
    print(s)

start = time()
myFun(201)
print(time() - start, "seconds")
