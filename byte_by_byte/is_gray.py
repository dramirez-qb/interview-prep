def is_gray(a, b):
    """
    Given two integers, determine whether they differ by a single bit
    """

    x = a ^ b
    return x & (x - 1) == 0


if __name__ == '__main__':
    print(is_gray(1, 2))
