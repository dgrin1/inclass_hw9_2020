from numpy import zeros,loadtxt
#load the ability to read data and make arrays

import matplotlib.pyplot as plt

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

y = loadtxt("trumpet.txt",float)
start_time = timeit.default_timer()
c = dft(y)
#c= rfft(y)
elapsed = timeit.default_timer() - start_time
print(elapsed)
plt.plot(abs(c))
#plot(abs(c),'r*')
plt.xlim(0,500)
plt.ylim(min(abs(c)),max(abs(c)))
plt.show()


