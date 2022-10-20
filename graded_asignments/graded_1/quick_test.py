from graded_asignments.graded_1.genetic_algorithm import GA
from console_actions import *

ga = GA(pop_size=100,
        mutate_treshold=0.2,
        generations=500,
        selection_scheme=ROULETTE,
        crossover_type=SINGLE_POINT,
        n_elites=50,
        thrust_value=870,
        low_level_mutation=False)
ga.run()
print(ga.population[0])
