import matplotlib.pyplot as plt
import numpy as np
import re

def transform(x_input,y_input):
	x_ans=[]
	y_ans=[]
	end = len(x_input)
	for k in np.arange(-10,10.1,0.1):
		p=0.0
		for i in range(0,end):
			l=1.0
			for j in range(0,end):
				if j != i:
					l=l*(round(k,4)-x_input[j])/(x_input[i]-x_input[j])
			
			p=p+y_input[i]*l
		x_ans.append(round(k,4))
		y_ans.append(p)
	
	return x_ans, y_ans
	
f = open('data.txt','r')
f1 = f.readlines()
x_input=[]
y_input=[]
for line in f1:
	line = re.findall(r"-*[0-9][0-9]*.[0-9][0-9]*",line)
	if len(line)==2:
		x_input.append(line[0])
		y_input.append(line[1])
	
x_input = np.array(x_input,dtype=np.float32)
y_input = np.array(y_input,dtype=np.float32)
f.close()

x_axis=[]
x_axis2=[]
y_axis=[]
y_axis2=[]
j=-10.0
for i in range(0,201):
	x_axis.append(j)
	y_axis2.append(j)
	x_axis2.append(0)
	y_axis.append(0)
	j+=0.1
	

x_ans, y_ans = transform(x_input,y_input)
plt.axis([-10,10,-10,10])
plt.plot(x_ans,y_ans,'r')
plt.plot(x_input,y_input,'bo')
plt.plot(x_axis,x_axis2,'g')
plt.plot(y_axis,y_axis2,'g')
plt.show()
