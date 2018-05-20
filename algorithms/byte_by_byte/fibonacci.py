def fib(n):
    '''
    Given n, compute the nth fibonacci number
    '''
    if n < 0:
        return -1
    if n == 0:
        return n

    memo = [-1] * (n + 1)
    memo[0] = 0
    memo[1] = 1
    return fib_helper(n, memo)

def fib_helper(n, memo):
    if memo[n] > -1:
        return memo[n]
    memo[n] = fib_helper(n - 1, memo) + fib_helper(n - 2, memo)
    return memo[n]

if __name__ == '__main__':
    n = int(input().strip())
    print(fib(n))
