def find_duplicates(arr):
    """
    Given an array of integers, where each value 1 <= x <= len(array), write a function that finds all duplicates in the array.

    Ex.
    [1, 2, 2, 4, 3, 1, 5] len=7
                       ^
     seen = {1, 2, 4, 3, 5}
     dups = [2, 1]
    Iterate through array
    Add to a set of seen values
    If a value is in seen, add it to a dups array
    O(n) O(n)
    """
    if len(arr) < 2:
        return []

    dups = set()

    for num in arr:
        index = abs(num) - 1
        if arr[index] < 0:
            dups.add(abs(num))
        else:
            arr[index] = -arr[index]

    for num in arr:
        num = abs(num)

    return list(dups)


if __name__ == '__main__':
    arr = [1, 2, 2, 4, 3, 1, 5]
    print(find_duplicates(arr))
