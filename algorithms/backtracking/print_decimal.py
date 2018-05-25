def print_decimal(digits, prefix=''):
    # print(f'print_binary({digits}, {prefix})')
    '''
    Print all permutations of the decimal numbers with n digits.
    2
    00
    01
    02
    03
    04
    05
    06
    07
    08
    ...
    '''

    if digits == 0:
        print(prefix)
    else:
        for i in range(10):
            print_decimal(digits - 1, prefix + str(i))

if __name__ == '__main__':
    digits = int(input().strip())
    print_decimal(digits)
