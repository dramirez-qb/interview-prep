def fib(n):
    """
    Given a number compute the nth fibonacci number

    fib(6)
    112358

    O(n) O(n)
    """
    if n < 0:
        raise ValueError('Only numbers greater than 0')
    memo = [None] * (n+1)
    return fib_helper(n, memo)


def fib_helper(n, memo):
    if n == 0 or n == 1:
        return n
    else:
        if not memo[n]:
            memo[n] = fib_helper(n - 1, memo) + fib_helper(n - 2, memo)
    return memo[n]


if __name__ == '__main__':
    print(fib(6))
