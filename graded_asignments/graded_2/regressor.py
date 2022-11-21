import math
import random

from sklearn.tree import DecisionTreeRegressor


class Regressor(DecisionTreeRegressor):
    def __init__(self):
        super().__init__()
        self.tree = self.get_randomly_initiated_tree()

    def get_randomly_initiated_tree(self):
        model = DecisionTreeRegressor()
        model.criterion = random.sample(["squared_error", "friedman_mse", "absolute_error", "poisson"], 1)
        model.splitter = random.sample(['best', 'random'], 1)
        return model
