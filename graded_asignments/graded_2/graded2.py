import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor


def read_data(path):
    return pd.read_csv(path)


def make_dataset(data, window_size=4):
    x, y = [], []
    for i in range(len(data) - window_size):
        x.append(data[i:i + window_size])
        y.append(data[i + window_size])
    return x, y


def plot_data():
    ax1 = pd_2022.plot(y='Demand')
    pd_2021.plot(y='Demand', grid=True, rot=90, ax=ax1)
    ax1.legend(['demand 2022', 'demand 2021'])
    plt.show()


def plot_2021_pred(pd_2021, predictions):
    ax1 = pd_2021.plot(y='Demand')
    df_pred = pd.DataFrame(predictions, columns=['Prediction'])
    df_pred.plot(grid=True, rot=90, ax=ax1)
    plt.show()


# Task 2b
def regression_trainer(rnd_seed):
    # legg in random variables etterhvert
    model = DecisionTreeRegressor(random_state=rnd_seed)
    return model


def predict_2021(window_size):
    pred_2021 = [0 for i in range(window_size)]
    for window in x:
        pred = model.predict([window])
        pred_2021.append(pred[0])
    plot_2021_pred(pd_2021, pred_2021)


def random_forest(size):
    forest = []
    for i in range(size):
        forest.append(regression_trainer(i))
    return forest


def bootstrapping():
    pass


def split_all_data(datasets):
    test_data = []
    train_data = []

    all_data = pd.concat([dataset for dataset in datasets])
    for sample in all_data['Demand']:
        if random.random() < 0.2:
            test_data.append(sample)
        else:
            train_data.append(sample)
    return test_data, train_data


def pick_random_samples_from_data(data):
    samples = []
    for sample in data:
        if random.random() < 0.5:
            samples.append(sample)
    return samples


if __name__ == '__main__':
    # import data
    pd_2021 = read_data('data/data_2021.csv')
    pd_2022 = read_data('data/data_2022.csv')
    np_2021 = pd_2021['Demand'].to_numpy()
    np_2022 = pd_2022['Demand'].to_numpy()
    # n_remaining_days = len(np_2021) - len(np_2022)
    window_size = 5
    plot_data()

    x, y = make_dataset(np_2021, window_size)
    model = regression_trainer(0)
    model.fit(x, y)

    # Task 2c
    predict_2021(window_size)
    test_data, train_data = split_all_data([pd_2021, pd_2022])

    # TASK 3
    m = 100  # n_classifiers
    forest = random_forest(m)  # create set of m classifiers

    # training the ensemble
    print("training...", end='')
    for tree in forest:
        bootstrap_data = pick_random_samples_from_data(train_data)
        x, y = make_dataset(bootstrap_data, window_size)
        tree.fit(x, y)
        print('.', end='')
    # print(forest)

    # AGGREGATION

    x, y = make_dataset(np_2021, window_size)
    # de må predicte med samme vindu
    complete_pred = []
    for window in x:
        current_predictions = []
        for tree in forest:
            pred = [0 for i in range(window_size)]
            pred = tree.predict([window])
            current_predictions.append(pred[0])
        avg = sum(current_predictions) / len(current_predictions)
        complete_pred.append(avg)
    print("finished")

    pd_ensemble_pred = pd.DataFrame(complete_pred)
    ax1 = pd_2021.plot(y='Demand')
    pd_ensemble_pred.plot(grid=True, rot=90, ax=ax1)
    ax1.legend(['demand 2021', 'prediction'])
    plt.show()


    # plt.plot(complete_pred, color='green')
    # plt.plot(np_2021)
    # plt.show()

