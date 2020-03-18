from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show

def f(x,t):
    return -x**3 + sin(t)

a = 0.0           # Start of the interval
b = 10.0          # End of the interval
N = 1000          # Number of steps
h = (b-a)/N       # Size of a single step
x = 0.0           # Initial condition

#Euler's method using -- using slope at one point
tpoints = arange(a,b,h)
xpoints = []
for t in tpoints:
    xpoints.append(x)
    x += h*f(x,t)
#plot right here
plot(tpoints,xpoints,'ko')
xlabel("t")
ylabel("x(t)")

#set same region with smaller number points
a = 0.0
b = 10.0
N = 100
h = (b-a)/N

#create list of points rranged by step size
tpoints = arange(a,b,h)
x2points = []

x = 0.0
#loop over time
for t in tpoints:
    x2points.append(x)
 #two estimates of slope, used to compute average slope and take a better step
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    x += k2
#plot better estimate
plot(tpoints,x2points,'r--')



#runge kutta 4

a = 0.0
b = 10.0
#I can do just as well, using only 40 points
N = 40
h = (b-a)/N

tpoints = arange(a,b,h)
x4points = []
x = 0.0

for t in tpoints:
    x4points.append(x)
#4 estimates of the step
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6

plot(tpoints,x4points,'m*')




show()
