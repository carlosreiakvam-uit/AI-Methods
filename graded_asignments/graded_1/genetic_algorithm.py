import random
from graded_asignments.graded_1.Chromosome import Chromosome
from constants import *


class GA:
    def __init__(self, pop_size, mutate_treshold, epochs, selection_scheme, crossover_type):
        self.population = []
        # settings
        self.pop_size = pop_size
        self.mutate_threshold = mutate_treshold
        self.epochs = epochs
        self.selection_scheme = selection_scheme
        self.crossover_type = crossover_type

        self.create_initial_population()

    # create initial population
    def create_initial_population(self):
        for i in range(self.pop_size):
            init_ind = Chromosome()
            init_ind.set_random_features()
            init_ind.set_fitness()
            self.population.append(init_ind)

        # sort population from best to worst
        self.population.sort(key=lambda x: x.fitness_val, reverse=True)

    def crossbreed(self, print_along=False):
        print("crossbreeding")
        for i in range(self.epochs):
            for j in range(1, self.pop_size - 1):
                ind_1 = self.population[j - 1]
                ind_2 = self.population[j + 1]
                crossover_features = ind_1.crossover(ind_2, crossover_type=self.crossover_type)
                ind_new = Chromosome(init_features=crossover_features)
                ind_new.set_fitness()
                if self.check_mutate_threshold(self.mutate_threshold):
                    ind_new.mutate()
                if self.selection_scheme == ELITISM:
                    self.population[len(self.population) - j] = ind_new  # replace least fit individual

            # sort population from best to worst
            self.population.sort(key=lambda x: x.fitness_val, reverse=True)
            if i % 1000 / self.epochs == 0:
                print('.', end='')
            if print_along:
                print(self.population[0])

    def check_mutate_threshold(self, rate):
        return random.random() < rate

    def print_population(self, head: float('inf')):
        print("\n\nPOPULATION")
        if head != float('inf'):
            print(f'Showing {head} best individuals')
        for i, p in enumerate(self.population):
            print(p)
            if i == head:
                break
