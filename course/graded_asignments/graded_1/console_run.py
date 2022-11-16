from constants import *
from genetic_algorithm import GA


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
        inp = demo_parameters()
    elif inp == 2:
        inp = get_user_input()
    elif inp == 3:
        return -1
    return inp


def input_mutation():
    while True:
        try:
            print("mutation rate :", end=' ')
            mutation_rate = float(input())
            if 1 >= mutation_rate >= 0:
                return mutation_rate
            else:
                print("enter a decimal number between 0 and 1")
        except ValueError:
            print("invalid input")


def input_selection_scheme():
    while True:
        try:
            print("selection scheme (1=elitism, 2=roulette):", end=' ')
            selection_scheme = int(input())
            if selection_scheme == 1 or selection_scheme == 2:
                return selection_scheme
            else:
                print("enter 1 or 2")
        except ValueError:
            print("invalid input")


def input_term_avg():
    while True:
        try:
            print("Termination at average (1=yes, 2=no):", end=' ')
            termination_condition = int(input())
            if termination_condition == 1:
                return True
            elif termination_condition == 2:
                return False
            else:
                print("enter 1 or 2")
        except ValueError:
            print("invalid input")


def input_n_generations():
    while True:
        try:
            print("n generations:", end=' ')
            generations = int(input())
            if 1000000 > generations >= 1:
                return generations
            else:
                print("enter a number between 1 and 1000000")
        except ValueError:
            print("invalid input")


def input_thrust():
    while True:
        try:
            print("optimize for thrust value:", end=' ')
            thrust_value = int(input())
            if 100000 > thrust_value >= 10:
                return thrust_value
            else:
                print("enter a number between 10 and 100000")
        except ValueError:
            print("invalid input")


def get_user_input():
    generations = 100  # initialize
    print("Please enter some values...")
    mutation_rate = input_mutation()
    selection_scheme = input_selection_scheme()
    term_cond = input_term_avg()
    input_n_generations()
    thrust_value = input_thrust()

    print("running algorithm, please wait...")

    return {'pop_size': 100,
            'mutation_threshold': mutation_rate,
            'generations': generations,
            'selection_scheme': selection_scheme,
            'crossover_type': MULTI_POINT,
            'n_elites': 90,
            'thrust_value': thrust_value,
            'term_cond': term_cond}


def demo_parameters() -> dict:
    print("\npopulation size:\t\t500")
    print("mutation rate:\t\t\t0.03")
    print("n generations:\t\t\t3000")
    print("selection scheme:\t\troulette")
    print("n elites:\t\t\t\t100")
    print("crossover type:\t\t\tmulti-point")
    print("seeking thrust value:\t870")
    print("termination average fitness:\t\tFalse")
    print("\nRunning demo algorithm...", end='')

    return {'pop_size': 500,
            'mutation_threshold': 0.03,
            'generations': 3000,
            'selection_scheme': ROULETTE,
            'crossover_type': MULTI_POINT,
            'n_elites': 100,
            'thrust_value': 870,
            'term_cond': False}


if __name__ == '__main__':
    inp = 0
    while True:
        inp = user_or_demo()
        if inp == -1:
            break
        elif inp == 0:
            continue
        else:
            ga = GA(pop_size=inp['pop_size'],
                    mutate_threshold=inp['mutation_threshold'],
                    generations=inp['generations'],
                    selection_scheme=inp['selection_scheme'],
                    crossover_type=inp['crossover_type'],
                    n_elites=inp['n_elites'],
                    thrust_value=inp['thrust_value'],
                    term_avg=inp['term_cond'])
            ga.run(print_along=True)
            print("\n\nRESULTS")
            print(ga.population[0])
            print("\n(enter to continue)", end='')
            input()
