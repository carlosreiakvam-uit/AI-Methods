import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from graded_asignments.graded_2.regressor import Regressor
from sklearn.tree import DecisionTreeRegressor


class Ensemble:
    def __init__(self):
        forest_size = 200
        self.forest = self.random_forest(forest_size)

    def random_forest(self, size) -> list:
        forest = []
        for i in range(size):
            regressor = Regressor()
            forest.append(regressor.tree)
        return forest

    def train_forest(self, train_data, window_size=10):
        print("training...", end='')
        for tree in self.forest:
            bootstrap_data = self.pick_random_samples_from_data(train_data)
            x, y = tree.slide_dataset(bootstrap_data, window_size)
            tree.fit(x, y)
            print('.', end='')
        print('Finished!', end='')

    def pick_random_samples_from_data(self, data) -> list:
        samples = []
        for sample in data:
            if random.random() < 0.5:
                samples.append(sample)
        return samples

    def bootstrap_aggregate(self, x, window_size) -> list:
        complete_pred = []
        for window in x:
            current_predictions = []
            for tree in self.forest:
                pred = [0 for i in range(window_size)]
                pred = tree.predict([window])
                current_predictions.append(pred[0])
            avg = sum(current_predictions) / len(current_predictions)
            complete_pred.append(avg)
        return complete_pred

    def plot_comparison(self, training, prediction) -> None:
        pd_ensemble_pred = pd.DataFrame(prediction)
        ax1 = training.plot(y='Demand')
        pd_ensemble_pred.plot(grid=True, rot=90, ax=ax1)
        ax1.legend(['demand 2021', 'prediction'])
        plt.show()
