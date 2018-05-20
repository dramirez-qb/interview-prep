def ones_in_binary(x):
    '''
    Find the number of ones in the binary representation of a number.
    '''

    sum = 0

    while x > 0:
        sum += x & 1
        x >>= 1

    return sum

if __name__ == '__main__':
    x = int(input().strip())

    print(ones_in_binary(x))
