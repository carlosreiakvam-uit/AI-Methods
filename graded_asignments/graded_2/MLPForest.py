from graded_asignments.graded_2.utils import *
from sklearn.neural_network import MLPRegressor


class MLPForest:
    def __init__(self, forest_size):
        self.forest = self.create(forest_size)

    def create(self, forest_size):
        forest = []
        for i in range(forest_size):
            regr = MLPRegressor(random_state=1, max_iter=1000)
            forest.append(regr)
        return forest

    def train(self, train_data, window_size):
        print("training...", end='')
        for tree in self.forest:
            bootstrap_data = pick_random_samples_from_data(train_data)
            x, y = slide(bootstrap_data, window_size)
            tree.fit(x, y)
            print('.', end='')
        print('Finished!', end='')

    def predict(self, x, window_size) -> list:
        complete_pred = []
        for window in x:
            current_predictions = []
            for tree in self.forest:
                pred = tree.predict([window])
                current_predictions.append(pred[0])
            avg = sum(current_predictions) / len(current_predictions)
            complete_pred.append(avg)
        return complete_pred
