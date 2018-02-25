print('importing permutation of palindrome')


def is_permutation_of_palindrome(phrase):
    """
    Returns if a phrase is a permutation of a palindrome
    Runtime
    O(n) O(1)
    """
    return max_one_odd(phrase) <= 1


def get_char_number(char):
    a = ord('a')
    z = ord('z')
    val = ord(char)
    if a <= val and val <= z:
        return val - a
    return -1


def max_one_odd(phrase):
    frequency_table = [0] * (ord('z') - ord('a') + 1)
    count_odd = 0
    for char in phrase:
        val = get_char_number(char)
        if val != -1:
            frequency_table[val] += 1
            if frequency_table[val] % 2 == 1:
                count_odd += 1
            else:
                count_odd -= 1
    return count_odd


if __name__ == "__main__":
    s = "tactcoapapa"
    print("{} {}".format(s, is_permutation_of_palindrome(s)))
