print('Importing mergesort module')


def mergesort(my_list):
    """
    Sort a list by sorting the left and right half and then merging them together in order.
    Runtime: O(n log(n))
             O(n) space
    """
    if len(my_list) < 2:
        return my_list
    helper = []
    mergesort_helper(my_list, helper, 0, len(my_list) - 1)


def mergesort_helper(my_list, helper, left_start, right_end):
    if left_start < right_end:
        middle = int((left_start + right_end) / 2)
        # sort left half of list
        mergesort_helper(my_list, helper, left_start, middle)
        # sort right half of list
        mergesort_helper(my_list, helper, middle + 1, right_end)
        # merge both halves
        merge_halves(my_list, helper, left_start, middle, right_end)


def merge_halves(my_list, helper, left_start, middle, right_end):
    helper = my_list[:]

    helper_left = left_start
    helper_right = middle + 1
    current = left_start

    """iterate through helper array. Compare the left and right half, copying the smaller element from the two halves into the original array"""
    while helper_left <= middle and helper_right <= right_end:
        if helper[helper_left] <= helper[helper_right]:
            my_list[current] = helper[helper_left]
            helper_left += 1
        else:
            my_list[current] = helper[helper_right]
            helper_right += 1
        current += 1

    # copy the rest of the left side of the array into target array
    remaining = middle - helper_left
    for i in range(remaining + 1):
        my_list[current + i] = helper[helper_left + i]


if __name__ == "__main__":
    my_list = [1, 5, 3, 2, 9, 0, 22, 33, 12, 11]
    print('unsorted list')
    print(my_list)
    mergesort(my_list)
    print('sorted list')
    print(my_list)
