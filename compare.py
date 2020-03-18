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

tpoints = arange(a,b,h)
xpoints = []
for t in tpoints:
    xpoints.append(x)
    x += h*f(x,t)

plot(tpoints,xpoints,'k')
xlabel("t")
ylabel("x(t)")

a = 0.0
b = 10.0
N = 100
h = (b-a)/N

tpoints = arange(a,b,h)
x2points = []

x = 0.0
for t in tpoints:
    x2points.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    x += k2

plot(tpoints,x2points,'r--')





a = 0.0
b = 10.0
N = 40
h = (b-a)/N

tpoints = arange(a,b,h)
x4points = []
x = 0.0

for t in tpoints:
    x4points.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6

plot(tpoints,x4points,'m')




show()
