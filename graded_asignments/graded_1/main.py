import random

from graded_asignments.graded_1.Chromosome import Chromosome


def print_population(head: float('inf')):
    print("\n\nPOPULATION")
    if head != float('inf'):
        print(f'Showing {head} best individuals')
    for i, p in enumerate(population):
        print(p)
        if i == head:
            break


def check_mutate_threshold(rate):
    return random.random() < rate


if __name__ == '__main__':
    population = []

    ELITISM = 0
    ROULETTE = 1

    UNIFORM = 0

    # settings
    pop_size = 100
    mutate_threshold = 0.1
    epochs = 100
    selection_scheme = ELITISM
    crossover_type = UNIFORM

    # create initial population
    for i in range(pop_size):
        init_ind = Chromosome()
        init_ind.set_random_features()
        init_ind.set_fitness()
        population.append(init_ind)

    # sort population from best to worst
    population.sort(key=lambda x: x.fitness_val, reverse=True)

    # crossbreed population and create new offspring
    for i in range(epochs):
        for j in range(1, pop_size - 1):
            ind_1 = population[j - 1]
            ind_2 = population[j + 1]
            if crossover_type == UNIFORM:
                crossover_features = ind_1.uniform_crossover(ind_2)
            ind_new = Chromosome(init_features=crossover_features)
            ind_new.set_fitness()
            if check_mutate_threshold(mutate_threshold):
                ind_new.mutate()
            if selection_scheme == ELITISM:
                population[len(population) - j] = ind_new  # replace least fit individual
        # sort population from best to worst
        population.sort(key=lambda x: x.fitness_val, reverse=True)
        print(population[0])

    # print 10 best fit in population
    print_population(head=30)
