print('importing string rotation')


def is_rotation(s1, s2):
    """
    Given two strings, check to see if s2 is a rotation of s1
    Runtime
    O(s1) O(s1)
    """

    if len(s1) == len(s2) and s1:
        new_s1 = s1 + s1
        if s2 in new_s1:
            return True
    return False


if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print("{} {} {}".format(s1, s2, is_rotation(s1, s2)))
