from random import choice, randint
import math as m
import numpy as np


class Features:
    def __init__(self):
        self.a = bin(randint(0, 45))  # blade angle
        self.b = bin(choice(np.array([2, 3, 4, 5])))  # n blades
        self.y = bin(randint(55, 75))  # air/fuel ratio, represented by * 0.01
        self.d = bin(randint(1000, 2000))  # propeller diameter
        self.t = bin(randint(5, 50))  # , idle valve position theta, represented by * 0.01


class Chromosome:
    def __init__(self, chromo_id):
        self.id = chromo_id
        self.it = 870  # Ideal thrust: 870N
        self.ftr = Features()
        self.fitness_val = float('inf')

    def get_mapped(self):
        return {'a': int(self.ftr.a, 2),
                'b': int(self.ftr.b, 2),
                'y': int(self.ftr.y, 2),
                'd': int(self.ftr.d, 2),
                't': int(self.ftr.y, 2)}

    def get_thrust(self):
        mv = self.get_mapped()
        return (m.pow(mv['a'], mv['b']) + m.log(mv['y'])) / (mv['d'] + m.pow(mv['t'], 3))

    def set_fitness(self):
        self.fitness_val = 1 / (self.it - self.get_thrust())

    def get_fitness(self):
        return self.fitness_val

    def crossover(self, other):
        pass
        # crossbreed using multi point cross breeding of two individuals

    def mutate(self):
        pass
        # mutate features to avoid getting studck in local mimima

    def __str__(self):
        mv = self.get_mapped()
        return str(f'Chromosome {self.id}\n'
                   f"a:{mv['a']}\n"
                   f"b:{mv['b']}\n"
                   f"y:{mv['y']}\n"
                   f"d:{mv['d']}\n"
                   f"t:{mv['t']}\n"
                   f'thrust: {self.get_thrust()}\n'
                   f'fitness: {self.fitness_val}\n')
