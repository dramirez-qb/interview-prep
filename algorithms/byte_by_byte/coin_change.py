print('importing coin change')


def change(n, coins):
    memo = [-1] * n
    return change_helper(n, coins, memo)


def change_helper(n, coins, memo):
    if n == 0:
        return 0
    else:
        min = n
        for coin in coins:
            if n - coin >= 0:
                if memo[n - coin] == - 1:
                    memo[n - coin] = change_helper(n - coin, coins, memo)
                ways = memo[n - coin]
                if min > ways + 1:
                    min = ways + 1
        return min


if __name__ == "__main__":
    n = 32
    coins = {25, 10, 5, 1}
    print(change(n, coins))
