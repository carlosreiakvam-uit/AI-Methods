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
    pop_size = 10
    for i in range(pop_size):
        population.append(Chromosome(i))

    for p in population:
        p.set_fitness()

    for p in population:
        print(p)
