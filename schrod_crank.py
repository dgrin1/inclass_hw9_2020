from numpy import empty,arange, linspace,real
import cmath 
from banded import banded
from operator import mul
from vpython import *
from matplotlib import pyplot as plt
plt.ion()




#Constants 
L=1.e-8
N=1000
a=L/N
m=9.109e-31
hbar=1.055e-34
x0=L/2
sigma=1.e-10
kappa=5.0e10
tmax=1.0e-14
yscale=1.e-9
framerate=100
h=1.e-18


C=1j*hbar/(4*m*a*a)
a1=1+2*h*C
a2=-h*C
b1=1-2*h*C
b2=h*C

#Create initial arrays of x and psi
x=linspace(0,L,N+1)
psi=list(map(exp,(-(x-x0)**2/(2*sigma**2))))
elist=1j*kappa*x
flist=list(map(cmath.exp,elist))
psi=list(map(mul,psi,flist))
psi[0]=psi[N]=0
lines = plt.plot(x, psi)
plt.xlim([x[0], x[-1]])
#plt.xlabel('x')
#plt.ylabel('u(x,t)')



#Create tridiagonal larray
A=empty([3,N-1],complex)
A[0,:]=a2
A[1,:]=a1
A[2,:]=a2

# #Main loop for CN method
i=0
for t in arange(0,tmax,h):
	i+=1
	v= list([psi[i] * b2+psi[i+1]*b1+b2*psi[i+2] for i in range(0,N-1)])
	psi[1:N]=banded(A,v,1,1)
	if (i%20==0):
		lines[0].set_ydata(psi[:])
		plt.pause(0.0000000001)
		plt.draw()

	
