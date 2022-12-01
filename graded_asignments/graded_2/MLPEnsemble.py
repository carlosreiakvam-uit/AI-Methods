from sklearn.neural_network import MLPRegressor
from Ensemble import Ensemble


class MLPEnsemble(Ensemble):
    def __init__(self, ensemble_size):
        self.ensemble = self.create(ensemble_size)
        super().__init__(self.ensemble)

    def create(self, forest_size):
        ensemble = []
        for i in range(forest_size):
            regr = MLPRegressor(max_iter=4000)
            ensemble.append(regr)
        return ensemble
