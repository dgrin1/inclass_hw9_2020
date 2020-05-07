from matplotlib import pyplot
N = 100
a = 1664525
c = 1013904223
m = 4294967296
x = 1
results = []

for i in range(N):
    x = (a*x+c)%m
    results.append(x)
pyplot.plot(results,"o")
pyplot.show()
