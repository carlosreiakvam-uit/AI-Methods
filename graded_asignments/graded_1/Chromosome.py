import random
from random import randint
import math as m
import numpy as np
from constants import *


class Chromosome:

    def __init__(self, init_features=None, thrust_value=870.0):
        self.perfect_thrust: float = thrust_value
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
            # air/fuel ratio, represented by  y * 0.01
            'y': {'val': None, 'min': 55, 'max': 75},
            # propeller diameter
            'd': {'val': None, 'min': 1000, 'max': 2000},
            # idle valve position theta, represented by t * 0.1
            't': {'val': None, 'min': 5, 'max': 50}
        }
        if init_features is not None:
            self.set_all_features(init_features)
        else:
            self.set_random_features()

        self.set_fitness()

    def set_random_features(self) -> None:
        """
        - Set chromosome's features to random values within legal values
        :return: None
        """
        for key in self.feature_keys:
            self.set_feature(key, randint(self.features[key]['min'], self.features[key]['max']))

    def set_all_features(self, features: dict) -> None:
        """
        :param features: dict of features to set for given chromosome
        :return: None
        """
        for key, val in features.items():
            self.set_feature(key, int(val, 2))

    def set_feature(self, key, val) -> None:
        """
        - set value to given feature
        :param key: key matching dictionary of features
        :param val: value candidate for feature
        :return: None
        """
        if val < self.features[key]['min']:
            val = self.features[key]['min']
        elif val > self.features[key]['max']:
            val = self.features[key]['max']

        self.features[key]['val'] = self.make_feature_max_bits_long(format(val, 'b'), key)

    def make_feature_max_bits_long(self, val, key) -> str:
        """
        - Every feature has a max-value and the bit-length of this value is of interest here.\n
        - Make sure given value has as many bits as n bits of max-value.

        :param val: candidate for new feature in binary format
        :param key: key for getting given feature from dictionary
        :return: string value of properly formatted binary feature
        """
        n_bits_max_value = int(self.features[key]['max']).bit_length()
        if len(val) < n_bits_max_value:
            delta = n_bits_max_value - len(val)
            for i in range(delta):
                val = '0' + val
        return val

    # noinspection PyTypeChecker
    def get_mapped(self, round_decimals=False):
        """
        - get binary feature values as valid floats
        :param round_decimals: round values to 2 decimals
        :return: binary feature values mapped and adjusted to correct int values
        """
        mapped = {'a': int(self.features['a']['val'], 2),
                  'b': int(self.features['b']['val'], 2),
                  'y': int(self.features['y']['val'], 2) * 0.01,
                  'd': int(self.features['d']['val'], 2),
                  't': int(self.features['t']['val'], 2) * 0.1}
        if round_decimals:
            for k, v in mapped.items():
                mapped[k] = round(v, 2)
        return mapped

    def set_fitness(self):
        """
        - Set fitness for chromosome given calculation of thrust using chromosome's feature values
        :return: None
        """
        # get mapped features in float format
        mv = self.get_mapped()

        # calculate thrust
        self.thrust = (m.pow(mv['a'], mv['b']) + m.log(mv['y'])) / (mv['d'] + m.pow(mv['t'], 3))

        delta_thrust = self.perfect_thrust - self.thrust

        if self.thrust == self.perfect_thrust:
            self.fitness_val = float('inf')
        else:
            self.fitness_val = 1 / delta_thrust  # lower delta thrust gives higher fitness value

    def crossover(self, other, crossover_type) -> dict:
        """
        - **Crossing two chromosome by using a crossbreed-pattern**.\n
        - The crossbreed-pattern consists of 0's and 1's.\n
        - For a list of bits representing a feature value:\n
          - if crossbreed pattern = 0: use first chromosome's bit \n
          - if crossbreed pattern = 1: use second chromosome's bit\n
        :param other: Another Chromosome
        :param crossover_type: 0= Arithmetic crossover, 1 = single point crossover, 2 = multi point crossover, 3 = uniform crossover
        :return:
        """
        if crossover_type == ARITHMETIC:
            crossbreed_pattern = list(np.random.randint(0, 2, self.n_features))
        elif crossover_type == SINGLE_POINT:
            crossbreed_pattern = [0, 0, 0, 1, 1]
        elif crossover_type == MULTI_POINT:
            crossbreed_pattern = [0, 1, 0, 1, 1]
        else:  # UNIFORM
            crossbreed_pattern = list(np.random.randint(0, 2, self.n_features))

        new_features = {'a': None, 'b': None, 'y': None, 'd': None, 't': None}
        for i, k in enumerate(self.feature_keys):
            if bool(crossbreed_pattern[i]):
                new_features[k] = self.features[k]['val']
            else:
                new_features[k] = other.features[k]['val']
        return new_features

    # noinspection PyUnboundLocalVariable
    def mutate(self) -> None:
        """
        - each features bit-values have a 50% chance of being mutated
        :return:None
        """
        for k, _ in self.features.items():

            #  v is a list of bit-values for the given feature
            v: list = list(self.features[k]['val'])

            # mutate digit if random gives a value over 0.5
            for i, digit in enumerate(v):
                if random.random() > 0.5:
                    if digit == '0':
                        v[i] = '1'
                    elif digit == '1':
                        v[i] = '0'

            # transform list v to a string representing binary value
            bin_val = ''
            for i in v: bin_val = bin_val + i

            # set feature value to that of binary string value
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
