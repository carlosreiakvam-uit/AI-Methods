import pandas as pd
import random


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


def make_dataset(data, window_size=4):
    x, y = [], []
    for i in range(len(data) - window_size):
        x.append(data[i:i + window_size])
        y.append(data[i + window_size])
    return x, y



