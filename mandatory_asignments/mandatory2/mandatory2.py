from math import fsum, sqrt
import pandas as pd

# Iris data link
URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
df_iris = pd.read_csv(URL,
                      header=None,
                      names=['sepal length', 'sepal width',
                             'petal length', 'petal width', 'class'])

# print(df_iris.head(20))
df_iris['class'] = pd.factorize(df_iris['class'])[0]


# KNN Algorithm
# 1. Calculate the distance


def distance(p, q) -> float:
    sum = 0
    for i in range(4):
        sum += pow(p[i] - q[i], 2)
    euclidean_distance = sqrt(sum)
    return euclidean_distance


for i in range(len(df_iris)):
    sub_dist = []
    for j in range(1, len(df_iris) - 1):
        sub_dist.append(distance(df_iris.iloc[i], df_iris.iloc[j]))
    sub_dist.sort()
    least = sub_dist[0]

# 2. Find the nearest neighbors
# 3. Make the predictions
