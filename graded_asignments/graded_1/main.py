from graded_asignments.graded_1.Chromosome import Chromosome

if __name__ == '__main__':
    # c = Chromosome()
    # a = c.fitness(c.a, c.b, c.y, c.d, c.t)
    # a = int(c.a, 2)
    # b = int(c.b, 2)
    # y = int(c.y, 2)
    # d = int(c.y, 2)
    # t = int(c.t, 2)
    # print(c.get_fitness())
    # a = c.fitness(c.a, c.b, c.y, c.d, c.t)
    # print(c.get_fitness())

    population = []
    pop_size = 100
    for i in range(pop_size):
        new_individual = Chromosome(i)
        new_individual.set_fitness()
        population.append(new_individual)
    for p in population:
        print(p)

    population.sort(key=lambda x: x.fitness_val, reverse=True)

    for j in range(1, 21):
        new_offspring: Chromosome = population[j - 1].crossover(population[j + 1])
        print(new_offspring)
        new_offspring.mutate()
        population[len(population) - j] = new_offspring  # replace least fit individual

