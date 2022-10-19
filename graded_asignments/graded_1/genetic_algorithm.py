import random
from graded_asignments.graded_1.Chromosome import Chromosome
from constants import *


class GA:
    def __init__(self, pop_size, mutate_treshold, generations, selection_scheme,
                 crossover_type, n_elitism_rounds=20, thrust_value=870):
        self.population = []

        # settings
        self.thrust_value = thrust_value
        self.pop_size = pop_size
        self.mutate_threshold = mutate_treshold
        self.generations = generations
        self.selection_scheme = selection_scheme
        self.crossover_type = crossover_type

        # set elitism range
        if n_elitism_rounds < self.pop_size:
            self.n_elitism_rounds = n_elitism_rounds
        else:
            self.n_elitism_rounds = pop_size - 1

        # create initial population
        self.create_initial_population()

    def create_initial_population(self):
        for i in range(self.pop_size):
            self.population.append(Chromosome(thrust_value=self.thrust_value))
        self.population.sort(key=lambda x: x.fitness_val, reverse=True)  # sort population from best to worst

    def crossbreed(self, print_along=False):
        for i in range(self.generations):
            for j in range(1, self.n_elitism_rounds):
                ind_1 = self.population[j - 1]
                ind_2 = self.population[j + 1]
                crossover_features = ind_1.crossover(ind_2, crossover_type=self.crossover_type)
                ind_new = Chromosome(init_features=crossover_features, thrust_value=self.thrust_value)

                if random.random() < self.mutate_threshold:
                    ind_new.mutate()

                if self.selection_scheme == ELITISM:
                    self.population[len(self.population) - j] = ind_new  # replace least fit individual

            # sort population from best to worst
            self.population.sort(key=lambda x: x.fitness_val, reverse=True)
            self.print_loading_dots(i)

            if print_along:
                print(self.population[0])

    def print_population(self, head: float('inf')):
        print("\n\nPOPULATION")
        if head != float('inf'):
            print(f'Showing {head} best individuals')
        for i, p in enumerate(self.population):
            print(p)
            if i == head:
                break

    def print_loading_dots(self, i):
        if i % 2000 == 1900:
            print()
        elif i % (int(self.generations / 200)) == 0:
            print('.', end='')