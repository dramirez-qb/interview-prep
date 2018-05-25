def print_binary(digits, prefix=''):
    # print(f'print_binary({digits}, {prefix})')
    '''
    Print all permutations of the binary numbers with n digits.
    2
    00
    01
    10
    11
    '''

    if digits == 0:
        print(prefix)
    else:
        print_binary(digits - 1, prefix + '0')
        print_binary(digits - 1, prefix + '1')

if __name__ == '__main__':
    digits = int(input().strip())
    print_binary(digits)
