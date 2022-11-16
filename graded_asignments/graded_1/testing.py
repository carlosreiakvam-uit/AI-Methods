from genetic_algorithm import GA
from constants import *
import matplotlib.pyplot as plt

pop_size = 100
mutate_threshold = 0.3
generations = 500


def run(n_tests, pop_size, mutate_threshold, generations):
    print("Running", end='')
    elitism = run_elitism(n_tests, pop_size, mutate_threshold, generations)
    roulette = run_roulette(n_tests, pop_size, mutate_threshold, generations)
    plot_ga(elitism, 'Elitist selection', 'elitism.png')
    plot_ga(roulette, 'Roulette selection', 'roulette.png')


def run_test(name, n_tests, pop_size=pop_size, mutate_threshold=mutate_threshold, generations=generations,
             selection_scheme=ROULETTE,
             crossover_type=MULTI_POINT, n_elites=50, thrust_value=870, low_level_mutation=False):
    thrust_lst = []
    fitness_lst = []
    print("...", end='')
    for i in range(n_tests):
        ga = GA(pop_size=pop_size,
                mutate_threshold=mutate_threshold,
                generations=generations,
                selection_scheme=selection_scheme,
                crossover_type=crossover_type,
                n_elites=n_elites,
                thrust_value=thrust_value,
                low_level_mutation=low_level_mutation,
                )
        ga.run()
        best_thrust = ga.population[0].thrust
        best_fitness = ga.population[0].fitness_val
        thrust_lst.append(best_thrust)
        fitness_lst.append(best_fitness)
        print('.', end='')
    return {'thrust': thrust_lst, 'fitness': fitness_lst, 'name': name}


def run_elitism(n_tests, pop_size, mutate_threshold, generations):
    n_tests = n_tests
    elit_arit = run_test('elitism, ar', n_tests, selection_scheme=ELITISM, crossover_type=ARITHMETIC, pop_size=pop_size,
                         mutate_threshold=mutate_threshold, generations=generations)
    elit_sp = run_test('elitism, sp', n_tests, selection_scheme=ELITISM, crossover_type=SINGLE_POINT, pop_size=pop_size,
                       mutate_threshold=mutate_threshold, generations=generations)
    elit_mp = run_test('elitism, mp', n_tests, selection_scheme=ELITISM, crossover_type=MULTI_POINT, pop_size=pop_size,
                       mutate_threshold=mutate_threshold, generations=generations)
    return [elit_arit, elit_sp, elit_mp]


def run_roulette(n_tests, pop_size, mutate_threshold, generations):
    rou_arit = run_test('roulette, ar', n_tests, selection_scheme=ROULETTE, crossover_type=ARITHMETIC,
                        pop_size=pop_size,
                        mutate_threshold=mutate_threshold, generations=generations)
    rou_sp = run_test('roulette, sp', n_tests, selection_scheme=ROULETTE, crossover_type=SINGLE_POINT,
                      pop_size=pop_size,
                      mutate_threshold=mutate_threshold, generations=generations)
    rou_mp = run_test('roulette, mp', n_tests, selection_scheme=ROULETTE, crossover_type=MULTI_POINT, pop_size=pop_size,
                      mutate_threshold=mutate_threshold, generations=generations)
    return [rou_arit, rou_sp, rou_mp]


def plot_ga(data, title, filename):
    for i, t in enumerate(data):
        plt.plot(t['thrust'], label=t['name'], linewidth=1)
    plt.grid()
    plt.title(title)
    plt.ylabel('thrust')
    plt.xlabel('separate runs of genetic algorithm')
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.savefig(filename)
    plt.show()
    plt.close()
