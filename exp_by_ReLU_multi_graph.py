import matplotlib.pyplot as plt
#from decimal import Decimal

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def draw_graph(step,color):
    x,y = [],[]
    sum=0

    for i,j in enumerate(frange(0,10,step)):
        x.append(i)
        for a in range(i):
            sum=sum+max(0,x[a])
        y.append(sum)
        sum=0

    plt.plot(x, y, color, linewidth=2)
    plt.title('Step Size = {}'.format(step))

# subplot(x,y,z) sırasıyla, x, bölgenin satır sayısını; y, sütun sayısını ve z ise alt grafiğimizin konumunu belirtir

plt.subplot(3,3,1)
draw_graph(3,"red")

plt.subplot(3,3,3)
draw_graph(2,"blue")

plt.subplot(3,3,7)
draw_graph(1.5,"black")

plt.subplot(3,3,9)
draw_graph(.47,"green")
plt.show()
