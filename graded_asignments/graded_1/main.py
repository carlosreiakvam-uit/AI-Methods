from graded_asignments.graded_1.genetic_algorithm import GA
from console_actions import *

from constants import *

if __name__ == '__main__':
    inp = user_or_demo()

    ga = GA(pop_size=inp['pop_size'],
            mutate_treshold=inp['mutation_threshold'],
            generations=inp['generations'],
            selection_scheme=inp['selection_scheme'],
            crossover_type=inp['crossover_type'],
            n_elitism_rounds=inp['n_elitism_rounds'],
            thrust_value=inp['thrust_value'])
    ga.crossbreed()
    print()
    print(ga.population[0])
