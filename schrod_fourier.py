from numpy import empty,arange, linspace,real,cos,sin,pi,zeros,array,ndarray
import cmath 
from dcst import dst, idst
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
tstep=1.e-18
C=pi*pi*hbar/(2*m*L*L)

# Create arrays
repsi=zeros(N,float)
impsi=zeros(N,float)

x=linspace(0,L,N)
#Set initial conditions
for n in range(1,N):
	xn=n*a
	x[n]=xn
	gauss=exp(-(xn-x0)**2/(2*(sigma**2)))
	repsi[n]=gauss*cos(kappa*xn)
	impsi[n]=gauss*sin(kappa*xn)



lines=plt.plot(x,ndarray.tolist(repsi))

#determine fourier coefficients
alpha=dst(repsi)
eta=dst(impsi)
b=empty(N,float)

i=0
for t in arange(0.0,tmax,tstep):
	i+=1
	for k in range(1,N):
 		angle=C*k*k*t
 		b[k]=alpha[k]*cos(angle)+eta[k]*sin(angle)
	repsi=idst(b)
	
	if (i%20 ==0):
		lines[0].set_ydata(ndarray.tolist(repsi[:]))
		plt.pause(0.0000000001)
		plt.draw()
