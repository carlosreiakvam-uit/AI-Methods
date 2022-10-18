import random
from random import choice, randint, sample
import math as m
import numpy as np


class Chromosome:

    def __init__(self, init_features=None):
        self.it: float = 870.0  # Ideal thrust: 870N
        self.thrust: float = 0.0
        self.fitness_val = float('inf')
        self.feature_keys = ['a', 'b', 'y', 'd', 't']
        self.n_features = 5

        # init features to min value
        self.features = {
            # blade angel
            'a': {'val': None, 'min': 0, 'max': 45},
            # n blades
            'b': {'val': None, 'min': 2, 'max': 5},
            # air/fuel ratio, represented by * 0.01
            'y': {'val': None, 'min': 55, 'max': 75},
            # propeller diameter
            'd': {'val': None, 'min': 1000, 'max': 2000},
            # idle valve position theta, represented by * -2.01
            't': {'val': None, 'min': 5, 'max': 50}
        }
        if init_features is not None:
            self.set_all_features(init_features)

    def set_random_features(self):
        for key in self.feature_keys:
            self.set_feature(key, randint(self.features[key]['min'], self.features[key]['max']))

    def make_feature_max_bits_long(self, candidate, key):
        n_bits = int(self.features[key]['max']).bit_length()
        if len(candidate) < n_bits:
            delta = n_bits - len(candidate)
            for i in range(delta):
                candidate = '0' + candidate
        return candidate

    def set_all_features(self, features: dict):
        for key, val in features.items():
            self.set_feature(key, int(val, 2))

    def set_feature(self, key, val):
        if val < self.features[key]['min']:
            candidate = self.features[key]['min']
        elif val > self.features[key]['max']:
            candidate = self.features[key]['max']
        else:
            candidate = val

        self.features[key]['val'] = self.make_feature_max_bits_long(format(candidate, 'b'), key)

    # noinspection PyTypeChecker
    def get_mapped(self, round_decimals=False):
        mapped = {'a': int(self.features['a']['val'], 2),
                  'b': int(self.features['b']['val'], 2),
                  'y': int(self.features['y']['val'], 2) * 0.01,
                  'd': int(self.features['d']['val'], 2),
                  't': int(self.features['t']['val'], 2) * 0.1}
        if round_decimals:
            for k, v in mapped.items():
                mapped[k] = round(v, 2)
        return mapped

    def set_thrust(self):
        mv = self.get_mapped()
        self.thrust = (m.pow(mv['a'], mv['b']) + m.log(mv['y'])) / (mv['d'] + m.pow(mv['t'], 3))

    def set_fitness(self):
        self.set_thrust()
        if self.thrust != self.it:
            self.fitness_val = 1 / (self.it - self.thrust)
        else:
            self.fitness_val = 1.00

    def feature_range_is_valid(self, key, val):
        return self.features[key]['min'] < val < self.features[key]['max']

    def str_to_bin(self, bin_str) -> bin:
        bin_val: bin = ''.join(format(ord(i), '08b') for i in bin_str)
        return bin_val

    def multi_point_crossover(self, other) -> dict:
        offspring_features = {'a': None, 'b': None, 'y': None, 'd': None, 't': None}
        for key in self.feature_keys:
            new_f = ''
            a = self.features[key]['val']
            b = other.features[key]['val']
            for i in range(len(a)):
                if bool(random.getrandbits(1)):
                    new_f += a[i]
                else:
                    new_f += b[i]
            offspring_features[key] = new_f
        return offspring_features

    def mutate(self):
        pass
        # mutate features to avoid getting stuck in local mimima

    def __str__(self):
        mv = self.get_mapped(round_decimals=True)
        return str(f'thrust: {round(self.thrust, 2)}\t\t'
                   f'fit: {round(self.fitness_val, 6)}\t'
                   f"a:{mv['a']}, "
                   f"b:{mv['b']}, "
                   f"y:{mv['y']}, "
                   f"d:{mv['d']}, "
                   f"t:{mv['t']}")
