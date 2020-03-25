import numpy as np
import matplotlib.pyplot as plt
#constants
g=9.81
a=0.0
b=10.0
N=500
h=(b-a)/N
target=1.e-5 #target accuracy

x=np.zeros(N+1,float) #end + internal points
delta=1.0 #fractional change between iterations, initially alrge

while delta>target:
	xp=np.empty(N+1,float) #current trial
	xp[0]=xp[N]=0.0 #ball hits ground at initial and final time
	xp[1:N]=0.5*(x[0:N-1]+x[2:N+1]+h*h*g) #implement finite difference formulae
	delta=max(abs(x-xp)) #calculate error worst point
	x=xp #update
	#print(delta,x[N/2])

plt.plot(np.linspace(a,b,N+1),x) #generate x solution but not velocity-- need to use finite difference to get
print('Initial velocity is ', (x[1]-x[0])/(h), 'm/s')
plt.ion()
plt.show()
