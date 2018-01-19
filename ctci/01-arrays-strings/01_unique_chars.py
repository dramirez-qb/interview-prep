print('importing unique chars module')


def all_unique_chars(s):
    """
    Returns if a s has all unique characters.
    Runtime
    O(s) O(a)
    """
    if len(s) > 256:
        return False

    ascii_codes = [False] * 256

    for char in s:
        code = ord(char)
        if ascii_codes[code]:
            return False
        ascii_codes[code] = True

    return True


if __name__ == "__main__":
    s = "atrouzw-._?e~x"
    s2 = "aa"
    print("{} {}".format(s, all_unique_chars(s)))
    print("{} {}".format(s2, all_unique_chars(s2)))
