import pandas as pd
import random
import matplotlib.pyplot as plt


def split(datasets):
    """
    :param datasets: list of datasets to be split
    :return: lists of test_data and train_data
    """
    test_data = []
    train_data = []

    all_data = pd.concat([dataset for dataset in datasets])
    for sample in all_data['Demand']:
        if random.random() < 0.2:
            test_data.append(sample)
        else:
            train_data.append(sample)
    return test_data, train_data


def slide(data, window_size=4):
    x, y = [], []
    for i in range(len(data) - window_size):
        x.append(data[i:i + window_size])
        y.append(data[i + window_size])
    return x, y


def pick_random_samples_from_data(data) -> list:
    samples = []
    for sample in data:
        if random.random() < 0.5:
            samples.append(sample)
    return samples


def plot_comparison( training, prediction) -> None:
    pd_ensemble_pred = pd.DataFrame(prediction)
    ax1 = training.plot(y='Demand')
    pd_ensemble_pred.plot(grid=True, rot=90, ax=ax1)
    ax1.legend(['demand 2021', 'prediction'])
    plt.show()
