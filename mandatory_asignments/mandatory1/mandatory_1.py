coins = [1, 10, 5, 20]
total_amount = 1040528


def min_coins(coins: list, total_amount: int) -> int:
    """
    :param coins: list of coin values
    :param total_amount: total amount that you want to find minimum coin change for
    :return: int representing minimum amount of coins needed
    """
    table: list = [0]  # initialize table
    for amount in range(1, total_amount + 1):
        sub_problem = []  # initialize/reset list of sub problems
        for coin in coins:  # iterate over sub problems
            if coin <= amount:
                sub_problem.append(table[amount - coin])  # append value of sub problem to list of sub problems
        table.append(min(sub_problem) + 1)  # append min of sub problems to table
    return table.pop()  # return last element of table


print(min_coins(coins, total_amount))
