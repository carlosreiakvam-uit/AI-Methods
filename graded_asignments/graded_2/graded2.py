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


def regression_trainer(window):
    return model.predict([window])[0]


if __name__ == '__main__':
    # import data
    pd_2021 = read_data('data_2021.csv')
    pd_2022 = read_data('data_2022.csv')
    np_2021 = pd_2021['Demand'].to_numpy()
    np_2022 = pd_2022['Demand'].to_numpy()
    # n_remaining_days = len(np_2021) - len(np_2022)
    window_size = 5

    x, y = make_dataset(np_2021, window_size)
    model = DecisionTreeRegressor(random_state=0)
    model.fit(x, y)

    predictions = [0 for i in range(window_size)]
    for window in x:
        # prediction = model.predict([window])
        predictions.append(regression_trainer(window))

    plt.plot(np_2021, color="green")
    plt.plot(predictions, color="blue")
    plt.show()
