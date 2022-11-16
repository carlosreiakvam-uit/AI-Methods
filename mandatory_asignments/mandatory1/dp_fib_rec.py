def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_memo(n, memo):
    if n <= 1:
        return n
    elif (memo[n] == -1):
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_tabu_carl(n):  # n = 9
    tab = [0] * (n + 1)  # 10
    tab[0] = 0
    tab[1] = 1
    for i in range(2, n + 1):  # 8 iterations
        tab[i] = tab[i - 1] + tab[i - 2]
    return tab[n]


def fib_tabu_teacher(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    fib_number = 9
    print("fib number:\t", fib_number)

    # fib recursive
    print("fib rec:\t", fib_rec(fib_number))

    # fib memoization
    init_memo_list = [-1] * (fib_number + 2)
    print("fib memo:\t", fib_memo(fib_number, init_memo_list))

    # fib tabular carl
    print("fib tabulation:\t", fib_tabu_carl(fib_number))

    # fib tabular teacher
    print("fib tabulation:\t", fib_tabu_teacher(fib_number))
