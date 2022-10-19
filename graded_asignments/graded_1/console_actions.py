from constants import *


def user_or_demo():
    print("\n\nWelcome to genetic algorithm")
    print(
        """run demo.......1
user-input.....2
exit...........3""")
    print('choice: ', end='')
    try:
        inp = int(input())
    except ValueError:
        return 0

    if inp == 1:
        inp = use_standard_inputs()
    elif inp == 2:
        inp = get_user_input()
    elif inp == 3:
        return -1
    return inp


def get_user_input():
    generations = 100  # initialize
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
            'n_elitism_rounds': 90,
            'thrust_value': thrust_value}


def use_standard_inputs() -> dict:
    print("\npopulation size:\t\t100")
    print("mutation rate:\t\t\t0.2")
    print("n generations:\t\t\t10000")
    print("selection scheme:\t\telitism")
    print("n elitist gens:\t\t\t90")
    print("crossover type:\t\t\tmulti point")
    print("seeking thrust value:\t870")
    print("\nrunning demo algorithm...", end='')

    return {'pop_size': 100,
            'mutation_threshold': 0.2,
            'generations': 9999,
            'selection_scheme': ELITISM,
            'crossover_type': MULTI_POINT,
            'n_elitism_rounds': 90,
            'thrust_value': 870}
