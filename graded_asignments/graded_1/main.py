from graded_asignments.graded_1.genetic_algorithm import GA
from console_actions import *

if __name__ == '__main__':
    inp = 0
    while True:
        inp = user_or_demo()
        if inp == -1:
            break
        elif inp == 0:
            continue
        else:
            ga = GA(pop_size=inp['pop_size'],
                    mutate_treshold=inp['mutation_threshold'],
                    generations=inp['generations'],
                    selection_scheme=inp['selection_scheme'],
                    crossover_type=inp['crossover_type'],
                    n_elites=inp['n_elites'],
                    thrust_value=inp['thrust_value'])
            ga.run()
            print("\n\nRESULTS")
            print(ga.population[0])
            print("\n(enter to continue)", end='')
            input()

