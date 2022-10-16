from random import choice, randint
import math as m
import numpy as np


class Chromosome:
    def __init__(self):
        # initial values of first generation are created randomly
        # they are represented as binary numbers
        self.it = 870  # Ideal thrust: 870N
        self.a = bin(randint(0, 45))  # blade angle
        self.b = bin(choice(np.array([2, 3, 4, 5])))  # n blades
        self.y = bin(randint(55, 75))  # air/fuel ratio, represented by * 0.01
        self.d = bin(randint(1000, 2000))  # propeller diameter
        self.t = bin(randint(5, 50))  # , idle valve position theta, represented by * 0.01
        self.fitness_val = 0

    def thrust(self, a, b, y, d, t):
        return (m.pow(a, b) + m.log(y)) / (d + m.pow(t, 3))

    def fitness(self, a, b, y, d, t):
        self.fitness_val = self.it - self.thrust(int(a, 2), int(b, 2), int(y, 2), int(d, 2), int(t, 2))

    def get_fitness(self):
        return self.fitness_val

    def crossover(self, other):
        pass
        # crossbreed using multi point cross breeding of two individuals

    def mutate(self):
        pass
        # mutate features to avoid getting studck in local mimima
