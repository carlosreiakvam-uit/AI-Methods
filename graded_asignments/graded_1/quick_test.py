from graded_asignments.graded_1.genetic_algorithm import GA
from console_run import *

ga = GA(pop_size=100,
        mutate_threshold=0.2,
        generations=1000,
        selection_scheme=ROULETTE,
        crossover_type=MULTI_POINT,
        n_elites=100,
        thrust_value=870,
        low_level_mutation=True)
ga.run(print_along=True)
print("\nbest result")
print(ga.population[0])
