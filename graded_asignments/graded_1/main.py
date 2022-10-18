from graded_asignments.graded_1.genetic_algorithm import GA
from constants import *

if __name__ == '__main__':
    ga = GA(pop_size=100, mutate_treshold=0.2, epochs=1000, selection_scheme=ELITISM, crossover_type=MULTI_POINT)
    ga.crossbreed(print_along=True)
