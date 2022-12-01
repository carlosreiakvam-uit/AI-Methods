from sklearn.tree import DecisionTreeRegressor
from Ensemble import Ensemble
import random


class DTForest(Ensemble):
    def __init__(self, forest_size):
        self.forest = self.create(forest_size)
        super().__init__(self.forest)

    def create(self, forest_size):
        forest = []
        for i in range(forest_size):
            tree = DecisionTreeRegressor(
                criterion=random.choice(["squared_error", "friedman_mse", "absolute_error", "poisson"]),
                splitter=random.choice(['best', 'random'])
            )
            forest.append(tree)
        return forest
