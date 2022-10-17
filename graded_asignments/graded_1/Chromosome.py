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
    def __init__(self, chromosome_id):
        self.id: int = chromosome_id
        self.it: float = 870.0  # Ideal thrust: 870N
        self.ftr = Features()
        self.thrust: float = 0.0
        self.fitness_val = float('inf')
        self.mv = self.get_mapped()

    def get_mapped(self):
        return {'a': int(self.ftr.a, 2),
                'b': int(self.ftr.b, 2),
                'y': int(self.ftr.y, 2) * 0.01,
                'd': int(self.ftr.d, 2),
                't': int(self.ftr.y, 2) * 0.01}

    def set_thrust(self):
        mv = self.mv
        self.thrust = (m.pow(mv['a'], mv['b']) + m.log(mv['y'])) / (mv['d'] + m.pow(mv['t'], 3))

    def set_fitness(self):
        # self.set_thrust()
        self.thrust = 200
        if self.thrust != self.it:
            self.fitness_val = 1 / (self.it - self.thrust)
        else:
            self.fitness_val = 1.00

    def crossover(self, other):
        return self
        # crossbreed using multi point cross breeding of two individuals

    def mutate(self):
        pass
        # mutate features to avoid getting stuck in local mimima

    def __str__(self):
        mv = self.mv
        return str(f'Chromosome {self.id}\n'
                   f"a:{mv['a']}\n"
                   f"b:{mv['b']}\n"
                   f"y:{mv['y']}\n"
                   f"d:{mv['d']}\n"
                   f"t:{mv['t']}\n"
                   f'thrust: {self.thrust}\n'
                   f'fitness: {self.fitness_val}\n')
