from numpy import loadtxt,empty
from matplotlib.pyplot import scatter,show,xlim,plot,ion
from scipy.optimize import curve_fit
ion()

#Read and plot data the data
data=loadtxt("millikan.txt",float)
x=data[:,0]
y=data[:,1]
scatter(x,y)
xlim(0,1.3e15)

#do fitting
n=len(x)
Ex=0.0
Ey=0.0
Exx=0.0
Exy=0.0

#Compute relevant sums
for i in range(n):
	Ex +=x[i]
	Ey +=y[i]
	Exx+= x[i]*x[i]
	Exy+= x[i]*y[i]

Ex /= n
Ey /= n
Exx /= n
Exy /= n

denom=Exx-Ex*Ex
m=(Exy-Ex*Ey)/denom
c=(Exx*Ey-Ex*Exy)/denom
print("Slope=",m)


#Compare fit with data
yfit=empty(n,float)
for i in range(n):
	yfit[i]=m*x[i]+c


#do my own scipy fit, using full nonlinear algorithm
def lin(x,m,c):
	return m*x+c

params,covar=curve_fit(lin,x,y)
ygfit=lin(x,*params)

plot(x,yfit)
plot(x,ygfit,'r--')

print(m,c)
print(params)

show()
	
	
	
	






