import matplotlib.pyplot as plt

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def draw_graph(step,color):
    x,y = [],[]
    sum = 0

    #for i in frange(0,10,step):
    #    x.append(i)

    for i,j in enumerate(frange(0,10,step)):
        x.append(i)
        sum=sum+max(0,x[i])
        y.append(sum)
        
    print(x)
    print(y)

    plt.plot(x, y, color, linewidth=2)
    plt.title('Step Size = {}'.format(step))



draw_graph(1,"red")
plt.show()
