from utils import *


class Ensemble:

    def __init__(self, forest):
        self.forest = forest

    def bootstrap(self, data) -> list:
        samples = []
        for sample in data:
            if random.random() < 0.5:
                samples.append(sample)
        return samples

    def predict(self, x) -> list:
        """
        :param x: input as list
        :return: prediction using aggregation and bagging
        """
        complete_pred = []
        for window in x:
            current_predictions = []
            # Aggregation
            for tree in self.forest:
                pred = tree.predict([window])
                current_predictions.append(pred[0])
            avg = sum(current_predictions) / len(current_predictions)
            # bagging #TODO sjekk om stemmer
            complete_pred.append(avg)
        return complete_pred

    def train(self, train_data, window_size):
        print("training...", end='')
        for tree in self.forest:
            bootstrap_data = self.bootstrap(train_data)
            x, y = slide(bootstrap_data, window_size)
            tree.fit(x, y)
            print('.', end='')
        print('Finished!', end='')
