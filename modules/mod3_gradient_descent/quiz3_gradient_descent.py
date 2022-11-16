import matplotlib.pyplot as plt
import numpy as np
import math as m
import pandas


def gradient_descent(start, learning_rate: float, n_iter: int):
    x = start  # a starting point
    x_values = []
    y_values = []
    primes = []
    decrease_steps = []
    for i in range(n_iter):
        # inspecting slope of x
        prime = q_prime(x)
        primes.append(prime)

        # getting new step to decrease in x values
        decrease_step = learning_rate * prime
        decrease_steps.append(decrease_step)

        x_values.append(x)
        y_values.append(q(x))

        # Set new step for next iteration of x
        x += decrease_step
    return [primes, decrease_steps, x_values, y_values]


def q(x):
    return ((x + 3) ** 2) * (1 - x)


def q_prime(x):
    return -m.pow((3 * x), 2) - (10 * x) - 3


def plot_q():
    start, end = -4, 1
    plt.plot(
        [i for i in range(start, end)],
        [q(i) for i in range(start, end)])


start = -1
learning_rate = 0.1
n_iter = 4

print(f"start: {start}\nlearning rate: {learning_rate}\niterations: {n_iter}")

[slopes, descents, x, y] = gradient_descent(start=start, learning_rate=learning_rate, n_iter=n_iter)

frame = np.array([slopes, descents, x, y])
frame = frame.reshape((len(x), 4))
# plot
plt.clf()
plt.close()
plt.scatter(x, y)  # gradient descent plot
plot_q()
plt.show()

pandaview = pandas.DataFrame(frame, columns=["Slope", "Decrease", "x", "y"])
print(pandaview)
