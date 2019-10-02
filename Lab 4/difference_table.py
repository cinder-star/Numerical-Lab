import numpy as np
import matplotlib.pyplot as plt

def getInput(filename=None):
    x = [1,2,3,4,5]
    y = [0, 7, 26, 63, 124]

    return x, y

def generateTable(x, y):
    table = []
    n = len(x)
    for i in range(n):
        temp = [0] * n
        temp = np.array(temp, dtype=np.float32)
        table.append(temp)

    for i in range(0, n):
        for j in range(0, n-i):
            if i == 0:
                table[j][j] = y[j]
            else:
                table[j+i][j] = (table[j+i][j+1]-table[j+i-1][j])/(x[j+i]-x[j])

    table = np.array(table, dtype = np.float32)
    return table

def getValue(table, x, point):
    n = table.shape[0]
    f = 0
    for i in range(n):
        z = table[i][0]
        for j in range(i):
            z = z*(point - x[j])
        f = f + z

    return f

def getPoly(x_start, x_end, table, x):
    x_graph=[]
    y_graph=[]
    for i in np.arange(x_start,x_end,0.1):
        x_graph.append(i)
        y_graph.append(getValue(table,x,i))

    return x_graph, y_graph

def plot_axes():
    x_axis=[]
    x_axis2=[]
    y_axis=[]
    y_axis2=[]
    j=-130.0
    for i in range(0,2601):
        x_axis.append(j)
        y_axis2.append(j)
        x_axis2.append(0)
        y_axis.append(0)
        j+=0.1

    plt.plot(x_axis,x_axis2,'g')
    plt.plot(y_axis,y_axis2,'g')
    
if __name__ == ('__main__'):
    x, y = getInput()
    table = generateTable(x,y)
    x_graph, y_graph = getPoly(-10.0,10.0, table, x)
    plt.plot(x_graph, y_graph, 'r')
    plt.plot(x,y,'bo')
    plot_axes()
    plt.axis([-10,10,-130,130])
    plt.show()
