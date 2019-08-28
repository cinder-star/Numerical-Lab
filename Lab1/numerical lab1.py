import matplotlib.pyplot as plt

x1 = []
y1 = []
y2 = []
y3 = []
x_inter = []
y_inter = []
thresh = -5.0
step = 0.1

for i in range (0,101):
	z = thresh+step*i
	z = round(z,5)
	x1.append(z)
	z1 = round(0.3*z+1,5)
	z2 = round(0.7*z+1,5)
	z3 = round(z*z-3*z*z*z,5)
	y1.append(z1)
	y2.append(z2)
	y3.append(z3)
	if z1==z2 and z2==z3:
		x_inter.append(z)
		y_inter.append(z1)

plt.plot(x1,y1,'y')
plt.plot(x1,y2,'b')
plt.plot(x1,y3,'g')
plt.plot(x_inter,y_inter,'ro')
plt.axis([-5,5,-30,30])
plt.show()
