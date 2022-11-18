from sklearn.tree import DecisionTreeRegressor


class Regressor:
    def __init__(self):
        self.tree = self.get_randomly_initiated_tree()
        pass

    def get_randomly_initiated_tree(self):
        # legg in random variables etterhvert
        model = DecisionTreeRegressor(random_state=0)
        return model

    def slide_dataset(self, data, window_size=4):
        x, y = [], []
        for i in range(len(data) - window_size):
            x.append(data[i:i + window_size])
            y.append(data[i + window_size])
        return x, y

