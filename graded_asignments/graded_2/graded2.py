import pandas as pd
import matplotlib.pyplot as plt


def read_data(path):
    return pd.read_csv(path)


def trainRegressionsTree():
    pass


if __name__ == '__main__':
    # import data
    pd_2021 = read_data('data_2021.csv')
    pd_2022 = read_data('data_2022.csv')
    print(pd_2021)

    # split data

    # plot data
    ax1 = pd_2022.plot(y='Demand')
    pd_2021.plot(x='Date', y='Demand', grid=True, rot=30, ax=ax1)
    ax1.legend(['demand 2022', 'demand 2021'])

    plt.show()

    trainRegressionsTree()
