from constants import *


def user_or_demo() -> dict:
    print("Input own values or run demo with standard inputs (own values=1, demo=2): ")
    inp = int(input())
    if inp == 1:
        inp = get_user_input()
    else:
        inp = use_standard_inputs()
    return inp


def get_user_input():
    generations = 100  # initialize
    print("Welcome to genetic algorithm")
    print("Please enter some values...")
    print("mutation rate:", end=' ')
    mutation_rate = float(input())
    print("selection scheme (1=elitism, 2=roulette):", end=' ')
    selection_scheme = int(input())
    print("termination condition (1=n generations, 2=avg fitness):", end=' ')
    termination_condition = int(input())
    if termination_condition == 1:
        print("n generations:", end=' ')
        generations = int(input())
    print("optimize for thrust value:", end=' ')
    thrust_value = int(input())
    # print("average population fitness:", end=' ')
    # avg_pop_fit = int(input())
    return {'pop_size': 100,
            'mutation_threshold': mutation_rate,
            'generations': generations,
            'selection_scheme': selection_scheme,
            'crossover_type': MULTI_POINT,
            'n_elitism_rounds': 99,
            'thrust_value': thrust_value}


def use_standard_inputs() -> dict:
    print("population size:\t\t100")
    print("mutation rate:\t\t\t0.2")
    print("n generations:\t\t\t1000")
    print("selection scheme:\t\telitism")
    print("n elitist gens:\t\t\t99")
    print("crossover type:\t\t\tmulti point")
    print("seeking thrust value:\t870")
    print("running demo algorithm...", end='')

    return {'pop_size': 100,
            'mutation_threshold': 0.2,
            'generations': 1000,
            'selection_scheme': ELITISM,
            'crossover_type': MULTI_POINT,
            'n_elitism_rounds': 99,
            'thrust_value': 870}
