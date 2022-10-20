from graded_asignments.graded_1.genetic_algorithm import GA
from console_actions import *
from matplotlib import pyplot as plt


class Tester:
    def __init__(self):
        self.thrust_lst = []
        self.fitness_lst = []
        self.n_generations = 100

    def run_algo_n_times(self, n_generations):
        self.n_generations = n_generations
        self.thrust_lst = []
        self.fitness_lst = []
        for i in range(self.n_generations):
            ga = GA(pop_size=100,
                    mutate_treshold=0.2,
                    generations=500,
                    selection_scheme=ROULETTE,
                    crossover_type=MULTI_POINT,
                    n_elites=50,
                    thrust_value=870,
                    low_level_mutation=False)
            ga.run()
            best_thrust = ga.population[0].thrust
            best_fitness = ga.population[0].fitness_val
            self.thrust_lst.append(best_thrust)
            self.fitness_lst.append(best_fitness)
            print(best_thrust)

    def plot_thrust(self):
        b = [870 for i in range(100)]
        plt.plot(b)
        plt.plot(self.thrust_lst)
        plt.grid()
        plt.xlabel('100 attemptes of 500 generations each ')
        plt.ylabel('thrust')
        plt.show()


if __name__ == '__main__':
    tester = Tester()
    tester.run_algo_n_times(100)
    tester.plot_thrust()
