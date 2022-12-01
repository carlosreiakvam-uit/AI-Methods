from graded_asignments.graded_2.Ensemble import *
from sklearn.neural_network import MLPRegressor
from Ensemble import Ensemble


# Todo kan arve fra felles Ensemble for å dele på predict og resten av metodene fra predict
class MLPEnsemble(Ensemble):
    def __init__(self, ensemble_size):
        self.ensemble = self.create(ensemble_size)
        super().__init__(self.ensemble)

    def create(self, forest_size):
        ensemble = []
        for i in range(forest_size):
            regr = MLPRegressor(random_state=1, max_iter=1000)
            ensemble.append(regr)
        return ensemble
