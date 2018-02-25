print('Import quicksort module')


def quicksort(arr):
    """
    Sort a list of numbers using quicksort
    Runtime: O(n log n)
             O(log n) space
    """
    if len(arr) < 2:
        return arr
    quicksort_helper(arr, 0, len(arr) - 1)


def quicksort_helper(arr, start, end):
    """
    Run quicksort on each partition
    Runtime: O(log n)
    """
    if start >= end:
        return
    split_point = partition(arr, start, end)
    quicksort_helper(arr, start, split_point - 1)
    quicksort_helper(arr, split_point, end)


def partition(arr, start, end):
    """
    Partition the array with elements smaller than the pivot to the left and elements greater than the pivot to the right
    Runtime: O(n)
    """
    pivot = arr[(start + end) // 2]
    while start <= end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start <= end:
            swap(arr, start, end)
            start += 1
            end -= 1
    return start


def swap(arr, index1, index2):
    """
    Swap elements in list
    Runtime: O(1)
    """
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


if __name__ == "__main__":
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(arr)
    quicksort(arr)
    print('sorted')
    print(arr)
