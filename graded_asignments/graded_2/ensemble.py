import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor


class Ensemble:
    def __init__(self):
        forest_size = 200
        self.forest = self.random_forest(forest_size)

    def random_forest(self, size):
        forest = []
        for i in range(size):
            forest.append(self.get_tree(i))
        return forest

    def get_tree(self, rnd_seed):
        # legg in random variables etterhvert
        model = DecisionTreeRegressor(random_state=rnd_seed)
        return model

    def train_forest(self, train_data, window_size=10):
        for tree in self.forest:
            bootstrap_data = self.pick_random_samples_from_data(train_data)
            x, y = self.make_dataset(bootstrap_data, window_size)
            tree.fit(x, y)
            print('.', end='')

    def pick_random_samples_from_data(self, data):
        samples = []
        for sample in data:
            if random.random() < 0.5:
                samples.append(sample)
        return samples

    def make_dataset(self, data, window_size=4):
        x, y = [], []
        for i in range(len(data) - window_size):
            x.append(data[i:i + window_size])
            y.append(data[i + window_size])
        return x, y
