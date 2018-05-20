from collections import defaultdict

def anagrams(s1, s2):
    '''
    Given two strings, determine whether they are anagrams.
    '''

    if len(s1) != len(s2):
        return False

    s1 = s1.lower()
    s2 = s2.lower()

    letters = [0]*256

    for char in s1:
        letters[ord(char)] += 1

    for char in s2:
        letters[ord(char)] -= 1

    for count in letters:
        if count != 0:
            return False

    return True

if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()

    print(anagrams(s1, s2))
