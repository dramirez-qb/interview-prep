def fizz_buzz(x):
    '''
    Print numbers from 1 to x.
    If a number is divisible by 3 print "Fizz"
    If a number is divisible by 5 print "Buzz"
    If a number is divisible by both 3 and 5 print "FizzBuzz"
    Else print the original number.
    '''

    if x < 1:
        return 'Value must be greater than 1'

    for i in range(1, x + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':
    x = int(input())

    print(fizz_buzz(x))
