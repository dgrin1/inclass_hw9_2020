from numpy import zeros,loadtxt
#load the ability to read data and make arrays



from pylab import plot,xlim,show
#plotting tools

from cmath import exp,pi
#lets us take complex exponentials

from numpy.fft import rfft
#import a different FFT

#import code timing tools
import timeit

#defs

#FFT code
def dft(y):
#first we define the length of an array to be 
#number of data
    N = len(y)

#create complex array
    c = zeros(N//2+1,complex)
#all the fourier coefficients that we want    
    for k in range(N//2+1):
#evaluate the numerical integral
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c
#j is the sqrt(-1)

y = loadtxt("sunspots.txt",float)
c = dft(y)
d= rfft(y)

plot(abs(c))
xlim(0,500)
show()
#'''mycode = '''

#print timeit.timeit(stmt = mycode)
