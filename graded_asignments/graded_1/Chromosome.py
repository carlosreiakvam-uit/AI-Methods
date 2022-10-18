import random
from random import choice, randint, sample, randrange
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

    def uniform_crossover(self, other) -> dict:
        uniform_pattern = np.random.randint(0, 2, self.n_features)
        new_features = {'a': None, 'b': None, 'y': None, 'd': None, 't': None}
        for i, k in enumerate(self.feature_keys):
            if bool(uniform_pattern[i]):
                new_features[k] = self.features[k]['val']
            else:
                new_features[k] = other.features[k]['val']
        return new_features

    def arithmetic_crossover(self, other) -> dict:
        pass

    def single_point_crossover(self, other) -> dict:
        pass

    def multi_point_crossover(self, other) -> dict:
        # TODO: this is now uniform. change it.
        uniform_pattern = np.random.randint(0, 2, self.n_features)
        new_features = {'a': None, 'b': None, 'y': None, 'd': None, 't': None}
        for i, k in enumerate(self.feature_keys):
            if bool(uniform_pattern[i]):
                new_features[k] = self.features[k]['val']
            else:
                new_features[k] = other.features[k]['val']
        return new_features


    # noinspection PyUnboundLocalVariable
    def mutate(self):
        for k, v in self.features.items():
            bin_val = ''
            v: list = list(self.features[k]['val'])
            for i, digit in enumerate(v):
                if random.random() > 0.5:
                    if digit == '0':
                        v[i] = '1'
                    elif digit == '1':
                        v[i] = '0'
            # back to string
            for i in v:
                bin_val = bin_val + i
            self.features[k]['val'] = bin_val

    def __str__(self):
        mv = self.get_mapped(round_decimals=True)
        return str(f'thrust: {self.thrust}\t\t'
                   f'fit: {self.fitness_val}\t'
                   f"a:{mv['a']}, "
                   f"b:{mv['b']}, "
                   f"y:{mv['y']}, "
                   f"d:{mv['d']}, "
                   f"t:{mv['t']}")
