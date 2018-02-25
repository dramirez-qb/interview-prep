print('Import binary search module')


def binary_search_recursive(my_list, x):
    return binary_search_recursive_helper(my_list, x, 0, len(my_list) - 1)


def binary_search_recursive_helper(my_list, x, left, right):
    """
    Search for an element in a sorted array by searching through the middle and the halving the list each time.
    Runtime: O(log (n))
    """

    if left > right:
        return "Not found"

    mid = int((left + right) / 2)
    if my_list[mid] == x:
        return "{} found at position {}".format(my_list[mid], mid)
    elif x < my_list[mid]:
        return binary_search_recursive_helper(my_list, x, left, mid - 1)
    else:
        return binary_search_recursive_helper(my_list, x, mid + 1, right)


def binary_search_iterative(my_list, x):
    left = 0
    right = len(my_list) - 1

    while left <= right:
        mid = int((left + right) / 2)
        if my_list[mid] == x:
            return "{} found at position {}".format(my_list[mid], mid)
        elif x < my_list[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return "Not found"


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 7, 8, 11, 22, 33, 33, 34, 55]
    found = 34
    not_found = 56

    print('recursive')
    print(binary_search_recursive(my_list, found))
    print(binary_search_recursive(my_list, not_found))

    print('iterative')
    print(binary_search_iterative(my_list, found))
    print(binary_search_iterative(my_list, not_found))
