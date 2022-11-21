import matplotlib.pyplot as plt
from graded_asignments.graded_2.regressor import Regressor
from graded_asignments.graded_2.utils import *
from sklearn.tree import DecisionTreeRegressor


# criterion = random.sample(["squared_error", "friedman_mse", "absolute_error", "poisson"], 1),
# splitter = random.sample(['best', 'random'], 1))

class Ensemble:
    def __init__(self, forest_size=200):
        self.forest = self.create_forest(forest_size)

    def create_forest(self, forest_size):
        forest = []
        for i in range(forest_size):
            tree = DecisionTreeRegressor(
                criterion=random.choice(["squared_error", "friedman_mse", "absolute_error", "poisson"]),
                splitter=random.choice(['best', 'random'])
            )
            forest.append(tree)
        return forest

    def train_forest(self, train_data, window_size=10):
        print("training...", end='')
        for tree in self.forest:
            bootstrap_data = self.pick_random_samples_from_data(train_data)
            x, y = slide_dataset(bootstrap_data, window_size)
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

# if __name__ == '__main__':
#     pd_2021 = pd.read_csv('data/data_2021.csv')
#     pd_2022 = pd.read_csv('data/data_2022.csv')
#     np_2021 = pd_2021['Demand'].to_numpy()
#     np_2022 = pd_2022['Demand'].to_numpy()
#     ws = 10
#
#     x, y = make_dataset(np_2021, ws)
#
#     test_data, train_data = split_all_data([pd_2021, pd_2022])
#
#     ensemble = Ensemble()
#     ensemble.train_forest(train_data, window_size=ws)
