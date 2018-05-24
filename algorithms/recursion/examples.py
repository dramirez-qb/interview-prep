def fact(n):
    '''
    Compute the factorial for n
    5!
    5 * 4 * 3 * 2 * 1 * 0
    '''

    if n < 0:
        raise ValueError('negative not allowed')
    elif n == 0:
        return 1
    else:
        return n * fact(n - 1)

def power(base, exp):
    '''
    Compute the base to the exp power
    2^3
    2 * 2 * 2
    '''

    if exp < 0:
        raise ValueError('negative exponent not allowed')
    elif exp == 0:
        return 1
    elif exp % 2 == 0:
        return power(base * base, exp // 2)
    else:
        return base * power(base, exp - 1)

def is_palindrome(s):
    '''
    Determine if the given string is a palindrome.
    '''

    s = s.lower()
    return is_palindrome_helper(s)

def is_palindrome_helper(s):
    if len(s) <= 1:
        return True
    else:
        first = s[0]
        last = s[-1]
        if first == last:
            middle = s[1:-1]
            return is_palindrome_helper(middle)
    return False

def print_binary(n):
    '''
    Print the binary representation of a number
    '''
    if n < 0:
        print('-', end='')
        print_binary(-n)
    elif n <= 1:
        print(n, end='')
    else:
        last_digit = n % 2
        rest_of_digit = n // 2
        print_binary(rest_of_digit)
        print_binary(last_digit)

def fib(n):
    '''
    Compute the nth fibonacci number
    '''

    cache = {}
    return fib_helper(n, cache)

def fib_helper(n, cache):
    if n < 1:
        raise ValueError('negative not allowed')
    elif n <= 2:
        return 1
    elif n in cache:
        return cache.get(n)
    else:
        result = fib(n - 1) + fib(n - 2)
        cache[n] = result
        return result

def evaluate(exp):
    '''
    Evaluate the expression in the string
    (1 + ((2 * 3) + 4))
    11
    '''

    index = 0
    return eval_helper(exp, index)

def eval_helper(exp, index):
    print(f'eval_helper({exp}, {index})')
    if exp[index].isdigit():
        result = int(exp[index])
        print(f'base result {result}')
        index += 1
        return result
    else:
        index += 1 # skip (
        left = eval_helper(exp, index) # operand
        op = exp[index] # operator
        index += 1
        right = eval_helper(exp, index) # operand
        index += 1 # skip )

        if op == '+':
            result = left + right
        else:
            result = left * right
        print(f'recur result {result}')
        return result

if __name__ == '__main__':
    #n = int(input().strip())
    #base = int(input().strip())
    #exp = int(input().strip())
    #s = input().strip()
    exp = '((1+3)*(2*(4+1)))'
    #print(fact(n))
    #print(power(base, exp))
    #print(is_palindrome(s))
    #print_binary(n)
    #print(fib(n))
    print(evaluate(exp))
