import random
import numpy as np
from graded_asignments.graded_1.Chromosome import Chromosome
from constants import *


class GA:
    def __init__(self, pop_size, mutate_treshold, generations, selection_scheme,
                 crossover_type, n_elites=None, thrust_value=870, low_level_mutation=True):

        self.low_level_mutation = low_level_mutation
        self.population = []
        self.feature_keys = ['a', 'b', 'y', 'd', 't']
        self.n_features = 5

        # settings
        self.thrust_value = thrust_value
        self.pop_size = pop_size
        self.mutate_threshold = mutate_treshold
        self.generations = generations
        self.selection_scheme = selection_scheme
        self.crossover_type = crossover_type

        # set n elites range
        if n_elites is None or n_elites > self.pop_size:
            self.n_elites = int(self.pop_size * 0.5)
        else:
            self.n_elites = n_elites

        # create initial population
        self.create_initial_population()

    def create_initial_population(self):
        for i in range(self.pop_size):
            self.population.append(Chromosome(thrust_value=self.thrust_value))
        self.population.sort(key=lambda x: x.fitness_val)  # sort population from best to worst

    # noinspection PyUnboundLocalVariable
    def run(self, print_along=False):
        for i in range(self.generations):

            # iterate over population
            for j in range(1, self.n_elites):

                # SELECTION
                if self.selection_scheme == ROULETTE:
                    parent_1 = self.roulette()
                    parent_2 = self.roulette()
                elif self.selection_scheme == ELITISM:
                    parent_1 = self.population[j - 1]
                    parent_2 = self.population[j + 1]

                # CROSSBREEDING
                crossover_features = self.crossover(parent_1, parent_2, crossover_type=self.crossover_type)
                ind_offspring = Chromosome(init_features=crossover_features, thrust_value=self.thrust_value)

                # MUTATION
                if random.random() < self.mutate_threshold:
                    if self.low_level_mutation:
                        ind_offspring.low_level_mutation()
                    else:
                        ind_offspring.high_level_mutation()

                # REPLACEMENT
                self.population[len(self.population) - j] = ind_offspring  # replace least fit individual

                # sort population
                self.population.sort(key=lambda x: x.fitness_val)

        if print_along:
            print(self.population[0])

    def arithmetic_crossover(self, parent1, parent2):
        new_features = {'a': None, 'b': None, 'y': None, 'd': None, 't': None}
        for _, k in enumerate(self.feature_keys):
            f1_int = int(parent1.features[k]['val'], 2)
            f2_int = int(parent2.features[k]['val'], 2)
            mean = int((f1_int + f2_int) / 2)
            new_features[k] = format(mean, 'b')
        return new_features

    def multipoint_crossover(self):
        n_ones = random.randrange(1, self.n_features)
        ones = np.ones(n_ones, dtype=np.int8).tolist()
        zeros = np.zeros(self.n_features - n_ones, dtype=np.int8).tolist()
        pattern = ones + zeros
        random.shuffle(pattern)
        return pattern

    def singlepoint_crossover(self):
        n_ones = random.randint(1, self.n_features-1)
        ones = np.ones(n_ones, dtype=np.int8).tolist()
        zeros = np.zeros(self.n_features - n_ones, dtype=np.int8).tolist()
        pattern = ones + zeros
        return pattern

    def generate_features_from_crossover_pattern(self, pattern, parent1, parent2):
        new_features = {'a': None, 'b': None, 'y': None, 'd': None, 't': None}
        for i, k in enumerate(self.feature_keys):
            if pattern[i] == 0:
                new_features[k] = parent1.features[k]['val']
            else:
                new_features[k] = parent2.features[k]['val']
        return new_features

    def crossover(self, parent1: Chromosome, parent2: Chromosome, crossover_type) -> dict:
        """
        :param parent1: parent 1 Chromosome
        :param parent2: parent 2 Chromosome
        :param crossover_type: 0= Arithmetic crossover, 1 = single point crossover, 2 = multi point crossover, 3 = uniform crossover
        :return:
        """
        if crossover_type == ARITHMETIC:
            return self.arithmetic_crossover(parent1, parent2)
        elif crossover_type == SINGLE_POINT:
            pattern = self.singlepoint_crossover()
            return self.generate_features_from_crossover_pattern(pattern, parent1, parent2)
        elif crossover_type == MULTI_POINT:
            pattern = self.multipoint_crossover()
            return self.generate_features_from_crossover_pattern(pattern, parent1, parent2)
        else:  # UNIFORM
            pattern = list(np.random.randint(0, 2, self.n_features))
            return self.generate_features_from_crossover_pattern(pattern, parent1, parent2)

    def roulette(self):
        best_fitness = self.population[0].fitness_val  # closest to 0
        worst_fitness = self.population[-1].fitness_val  # furthest from 0
        diff = worst_fitness - best_fitness
        sum_fitness = 0
        try:
            random_roulette_n = random.randrange(best_fitness, worst_fitness)
        except ValueError:
            random_roulette_n = random.randrange(0, 1)
        for p in self.population:
            sum_fitness += p.fitness_val
            if sum_fitness > random_roulette_n:
                return p
        return self.population[0]  # failsafe return

    def print_population(self, head: float('inf')):
        print("\n\nPOPULATION")
        if head != float('inf'):
            print(f'Showing {head} best individuals')
        for i, p in enumerate(self.population):
            print(p)
            if i == head:
                break
