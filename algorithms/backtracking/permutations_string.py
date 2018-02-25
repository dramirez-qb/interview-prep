print('importing permutations module')


def permutations(s):
    permutations_helper(list(s), 0, len(s) - 1)


def permutations_helper(s, start, end):
    if start == end:
        print(to_string(s))
    else:
        for i in range(start, end + 1):
            s[start], s[i] = s[i], s[start]
            permutations_helper(s, start + 1, end)
            s[start], s[i] = s[i], s[start]


def to_string(s):
    return ''.join(s)


if __name__ == "__main__":
    s = 'javi'
    print(permutations(s))
