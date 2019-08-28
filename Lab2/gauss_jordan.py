import numpy as np
import re

step = 0

def get_var(num, i):
    f = open('var.txt','r')
    x = f.readline()
    x = x[0]
    f.close()
    if x >='A' and x<='Z':
        x = ord(x) - num + i +1
        x = chr(x)
        return str(x) + ': '
    return str(x)+str(i+1)+': '

def solve(matrix, b):
    f = open('result.txt','w')
    sz = matrix.shape
    for i in reversed(range(0,sz[0])):
        thresh = 0
        for j in range (i+1,sz[0]):
            thresh = thresh + matrix[i][j]
        matrix[i][i] = (b[i]-thresh)/matrix[i][i]
        vr = get_var(sz[0],i)
        f.write(vr+str(matrix[i][i])+'\n')
        for j in reversed(range(0,i)):
            matrix[j][i]=matrix[j][i]*matrix[i][i]
    f.close()

def correct_row(row, b_row, sz):
    if abs(b_row) == 0:
        b_row = 0
    for i in range(1,sz):
        if abs(row[i]) == 0:
            row[i]=0
    return row, b_row

def swap_rows(index,matrix,b):
    sz = matrix.shape
    for i in range(index+1,sz[0]):
        if abs(matrix[i][index]) > 0.000:
            matrix[[index,i]] = matrix[[i,index]]
            b[[index,i]] = b[[i,index]]

def print_matrix(matrix,b):
    sz = matrix.shape
    for i in range(0,sz[0]):
        x = matrix[i]
        y = b[i]
        x, y = correct_row(x,y,sz[0])
        np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
        print(x,end='')
        print(' | ',end='')
        np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
        print(y)        
    print()

def eliminate(index, matrix, b, bound):
    b[index] = b[index]/matrix[index][index]
    matrix[index] = matrix[index]/matrix[index][index]
    r = range(index+1,bound)
    for i in r:
        global step
        step = step+1
        print('Step: '+str(step))
        b[i] = b[i]-b[index]*matrix[i][index]
        matrix[i] = matrix[i]-matrix[index]*matrix[i][index]
        print_matrix(matrix,b)

    return matrix, b

def gauss_elimination(matrix, b):
    sz = matrix.shape
    for i in range(0,sz[0]):
        if abs(matrix[i][i]) <= 0.000:
            swap_rows(i,matrix,b)
        matrix, b = eliminate(i,matrix,b,sz[0])

    return matrix, b

def gauss_jordan_elimination(matrix, b):
    sz = matrix.shape
    for i in reversed(range(0,sz[0])):
        if abs(matrix[i][i]) <= 0.000:
            swap_rows(i,matrix,b)
        matrix, b = eliminate(i,matrix,b,True)

    return matrix, b

f = open('matrix.txt','r');
matrix = []
b = []
rows = 0

for line in f:
    row = [int(i) for i in line.split()]
    sz = len(row)
    b.append(row[sz-1])
    row = np.array(row[0:sz-1],dtype=np.float32)
    matrix.append(row)
    rows = rows + 1;

f.close()
b = np.array(b, dtype=np.float32)
matrix = np.array(matrix,dtype=np.float32)
matrix , b = gauss_elimination(matrix,b)
solve(matrix,b)