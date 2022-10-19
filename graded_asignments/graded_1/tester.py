from graded_asignments.graded_1.genetic_algorithm import GA
from console_actions import *
from matplotlib import pyplot as plt

if __name__ == '__main__':
    thrusts = []
    fitnesses = []
    for i in range(100):
        ga = GA(pop_size=100,
                mutate_treshold=0.03,
                generations=1000,
                selection_scheme=ROULETTE,
                crossover_type=MULTI_POINT,
                n_elites=50,
                thrust_value=870)
        ga.crossbreed()
        best_thrust = ga.population[0].thrust
        best_fitness = ga.population[0].fitness_val
        thrusts.append(best_thrust)
        fitnesses.append(best_fitness)
        print(best_thrust)
    plt.plot(fitnesses)
    plt.show()

