print('importing one away')


def one_edit_away(s1, s2):
    """
    Return if a string is one edit away from another (remove, insert, replace)
    Runtime
    O(n) O(1)
    """
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    return False


def one_edit_replace(s1, s2):
    found_difference = False
    for i in range(s1):
        if s1[i] != s2[i]:
            if found_difference:
                return False
            found_difference = True
    return True


def one_edit_insert(s1, s2):
    index1 = 0
    index2 = 0

    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


if __name__ == "__main__":
    s1 = "helloworld"
    s2 = "helloworld"
    print("{} {} {}".format(s1, s2, one_edit_away(s1, s2)))
