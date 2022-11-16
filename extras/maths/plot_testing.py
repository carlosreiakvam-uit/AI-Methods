import matplotlib.pyplot as plt
import math as m
import numpy as np

start =-1
end = 11
x = [i / 10 for i in range(start, end)]
y = [i**i for i in x]
plt.plot(x, y)
plt.show()
