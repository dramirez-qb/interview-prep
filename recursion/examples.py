print('recursion examples')

def countdown(n):
    try:
        if n < 1:
            raise ValueError

        print(n)
        if n > 1:
            countdown(n-1)
    except ValueError:
        print('Only positive integers')

def factorial(n):
    try:
        if n < 1:
            raise ValueError

        if n == 1:
            return 1
        else:
            return n * factorial(n-1)
    except ValueError:
        print('Only positive integers')

def fibonacci(n):
    try:
        if n < 0:
            raise ValueError
        memo = [None] * (n + 1)
        return fibonacci_helper(n, memo)
    except ValueError:
        print('Only positive integers')

def fibonacci_helper(n, memo):
    print('fibonacci_helper(' + str(n) + ')')
    if n == 0 or n == 1:
        return n
    if memo[n] is None:
        memo[n] = fibonacci_helper(n - 1, memo) + fibonacci_helper(n - 2, memo)
    return memo[n]

def power(base, exp):
    try:
        if exp < 0:
            raise ValueError

        if exp == 0:
            return 1
        else:
            return base * power(base, exp - 1)
    except ValueError:
        print('Only positive exponents')


def is_palindrome(phrase):
    phrase = phrase.lower()
    if len(phrase) <= 1:
        return True
    else:
        first_char = phrase[0]
        last_char = phrase[len(phrase) - 1]
        if first_char == last_char:
            return is_palindrome(phrase[1:len(phrase) - 1])
        else:
            return False

def decimal_to_binary(n):
    print('decimal_to_binary(' + str(n) +')')
    if n < 2:
        print(n)
    else:
        last_digit = n % 2
        rest_of_digit = n // 2
        decimal_to_binary(rest_of_digit)
        print(last_digit)


if __name__ == "__main__":
    #countdown(10)
    #print(factorial(4))
    print(fibonacci(5))
    #print(power(3, 5))
    #print(is_palindrome('RacecaR'))
    #print(decimal_to_binary(12))
