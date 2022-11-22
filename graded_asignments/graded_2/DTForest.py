from sklearn.tree import DecisionTreeRegressor
from graded_asignments.graded_2.utils import *
import random


class DTForest:
    def __init__(self, forest_size):
        self.forest = self.create(forest_size)

    def create(self, forest_size):
        forest = []
        for i in range(forest_size):
            tree = DecisionTreeRegressor(
                criterion=random.choice(["squared_error", "friedman_mse", "absolute_error", "poisson"]),
                splitter=random.choice(['best', 'random'])
            )
            forest.append(tree)
        return forest

    def train(self, data, window_size=10):
        print("training...", end='')
        for tree in self.forest:
            bootstrap_data = pick_random_samples_from_data(data)
            x, y = slide(bootstrap_data, window_size)
            tree.fit(x, y)
            print('.', end='')
        print('Finished!', end='')

    def predict(self, x) -> list:
        complete_pred = []
        for window in x:
            current_predictions = []
            for tree in self.forest:
                pred = tree.predict([window])
                current_predictions.append(pred[0])
            avg = sum(current_predictions) / len(current_predictions)
            complete_pred.append(avg)
        return complete_pred

    def predict2(self, initial_window: list, n_predictions: int) -> list:
        complete_pred = initial_window
        window = initial_window
        for i in range(n_predictions):
            current_predictions = []
            for tree in self.forest:
                pred = tree.predict([window])
                current_predictions.append(pred[0])
            avg_pred = sum(current_predictions) / len(current_predictions)
            # complete_pred.append(avg)
            window = window[1:]
            window.append(avg_pred)
            complete_pred.append(avg_pred)
        return complete_pred
