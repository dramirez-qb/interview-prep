print('importing check permutation')


def is_permutation(s1, s2):
    """
    Returns if a string is a permutation of another.
    Runtime:
    O(s) O(a)
    """

    if len(s1) != len(s2):
        return False

    ascii_codes = [0] * 256
    for char in s1:
        code = ord(char)
        ascii_codes[code] += 1

    for char in s2:
        code = ord(char)
        ascii_codes[code] -= 1
        if ascii_codes[code] < 0:
            return False

    return True


if __name__ == "__main__":
    s1 = "wookiewarrior"
    s2 = "kooweiarwroir"
    s3 = "aa"
    s4 = "bb"
    print("{} {} {}".format(s1, s2, is_permutation(s1, s2)))
    print("{} {} {}".format(s3, s4, is_permutation(s3, s4)))
