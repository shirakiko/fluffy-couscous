import random
import math
import matplotlib.pyplot as plt

num = 10000
num_in = 0
num_out = 0

xList = []
yList = []
cList = []
piList = []

for index in range(1,num+1):
    print(index) 
    x = random.random()
    y = random.random()
    xs = random.random() 
    x = x if xs>0.5 else -x  
    ys = random.random()
    if ys>0.5:
        y = y
    else:
        y = -y
    xList.append(x)
    yList.append(y)
    m = math.sqrt(x**2 + y**2)
    if m<1:
        num_in += 1
        cList.append('r')
    else:
        num_out += 1
        cList.append('b')
    piList.append(4 * num_in / index)
    print(4 * num_in / index)

plt.figure('p1') 
plt.plot(piList) 
plt.figure('p2') 
plt.scatter(xList,yList,c = cList)
plt.show()
