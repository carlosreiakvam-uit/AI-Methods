import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as sci


def gradient_descent(gradient, start, learn_rate: float, n_iter: int):
    """
    :param gradient: differential of function
    """
    slope = start
    x_gradient = []
    y_gradient = []
    for i in range(n_iter):
        diff = -learn_rate * Q_derivative(slope)
        slope += diff
        y_gradient.append(slope)
        x_gradient.append(Q(slope))
    return [y_gradient, x_gradient]


def Q(x):
    return ((x + 3) ** 2) * (1 - x)


def Q_derivative(x):
    return -((3 * x) ** 2) - 10 * x - 3


def parabola(x):
    return x ** 2


start = -4
end = 1
plt.plot(
    [i for i in range(start, end)],
    [Q(i) for i in range(start, end)])

# plot gradient descent
derivative = lambda v: -(3 * (v ** 2)) - (10 * v) - 3
[x_grad, y_grad] = gradient_descent(gradient=derivative, start=-1, learn_rate=0.5, n_iter=3)
plt.scatter(x_grad, y_grad)  # gradient descent plot
plt.show()

# print(y_grad)
# print(x_grad)
