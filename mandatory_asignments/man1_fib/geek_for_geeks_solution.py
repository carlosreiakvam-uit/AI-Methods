# A Dynamic Programming based Python3 program to
# find minimum of coins to make a given change V
import sys


# m is size of coins array (number of
# different coins)
def minCoins(coins, m, V):
    # table[i] will be storing the minimum
    # number of coins required for i value.
    # So table[V] will have result
    table = [0 for i in range(V + 1)]

    # Base case (If given value V is 0)
    table[0] = 0

    # Initialize all table values as Infinite
    for current_amount in range(1, V + 1):
        table[current_amount] = V

    # Compute minimum coins required
    # for all values from 1 to V
    for current_amount in range(1, V + 1):

        # Go through all coins smaller than i
        for j in range(m):
            if (coins[j] <= current_amount):
                sub_res = table[current_amount - coins[j]]
                if (sub_res != sys.maxsize and sub_res + 1 < table[current_amount]):
                    table[current_amount] = sub_res + 1

    if table[V] == sys.maxsize:
        return -1

    return table[V]


# Driver Code
if __name__ == "__main__":
    coins = [1, 5, 10, 20]
    m = len(coins)
    V = 99
    print("Minimum coins required is ",
          minCoins(coins, m, V))
