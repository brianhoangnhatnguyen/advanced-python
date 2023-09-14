import numpy
import matplotlib.pyplot as plot

speed = [34, 72, 19, 53, 65, 42, 87, 27, 60, 14, 95, 78, 46, 23, 68, 11, 88, 37, 99, 50]
x = numpy.mean(speed)
print(x)

y = numpy.median(speed)
print(y)

p = numpy.std(speed)
print(p)
something = [1, 1, 1, 2, 3, 7, 4, 9, 2, 8, 5, 8, 34, 7, 43, 7, 43, 78, 34, 7, 4, 78, 43, 7, 4, 8, 6, 3, 7, 9, 8, 43, 4, 7, 98, 65, 4]

plot.hist(something, bins=20, color="blue", edgecolor="navy", alpha=0.5)
plot.xlabel("value")
plot.ylabel("value")
plot.show()