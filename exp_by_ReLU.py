import matplotlib.pyplot as plt
#from decimal import Decimal

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step
x=[]
y=[]

for i in frange(0,10,.01):
    x.append(i)

sum=0
for i,j in enumerate(frange(0,10,.01)):
    for a in range(i):
        sum=sum+max(0,x[a])
    y.append(sum)
    sum=0

plt.plot(x,y)
plt.show()
