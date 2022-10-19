import random
from random import randint
import math as m
import numpy as np
from constants import *


class Chromosome:
    """
        **Features:**\n
        - a: blade angel between 0 and 45\n
        - b: n blades between 2 and 5\n
        - y: air/fuel ratio between 0.55 and 0.75\n
        - d: propeller diameter between 1000 and 2000\n
        - t: idle valve position theta between 0.5 and 55\n
    """

    def __init__(self, init_features=None, thrust_value=870.0):
        self.perfect_thrust: float = thrust_value
        self.thrust: float = 0.0
        self.fitness_val = float('-inf')
        self.feature_keys = ['a', 'b', 'y', 'd', 't']
        self.n_features = 5

        self.features = {
            'a': {'val': None, 'min': 0, 'max': 45},
            'b': {'val': None, 'min': 2, 'max': 5},
            'y': {'val': None, 'min': 55, 'max': 75},
            'd': {'val': None, 'min': 1000, 'max': 2000},
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

        # calculate fitness. Closer to 0 is better
        self.fitness_val = abs(self.perfect_thrust - self.thrust)

    def high_level_mutation(self) -> None:
        pass

    def low_level_mutation(self) -> None:
        """
        - each features bit-values have a 50% chance of being mutated
        :return:None
        """
        for k, _ in self.features.items():
            #  v is a list representation of bit-values for feature with key k
            v: list = list(self.features[k]['val'])
            bit_length = len(v)

            for i, digit in enumerate(v):
                if random.random() < 1 / bit_length:
                    # bit-flip
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
