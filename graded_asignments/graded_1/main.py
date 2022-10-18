from graded_asignments.graded_1.Chromosome import Chromosome

if __name__ == '__main__':
    population = []
    pop_size = 100

    # create initial population
    for i in range(pop_size):
        new_individual = Chromosome()
        new_individual.set_random_features()
        new_individual.set_fitness()
        population.append(new_individual)

    # sort population from best to worst
    population.sort(key=lambda x: x.fitness_val, reverse=True)

    # crossbreed population and create new offspring
    for j in range(1, pop_size - 1):
        crossover_features = population[j - 1].multi_point_crossover(population[j + 1])
        new_offspring = Chromosome(init_features=crossover_features)
        new_offspring.set_fitness()
        print(new_offspring)
        # new_offspring.mutate()
        # population[len(population) - j] = new_offspring  # replace least fit individual
    # print("finito")
