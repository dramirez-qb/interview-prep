def quicksort(arr):
    quicksort_helper(arr, 0, len(arr) - 1)


def quicksort_helper(arr, left, right):
    if left < right:
        pivot = arr[(left + right) // 2]
        partition_point = partition(arr, left, right, pivot)
        quicksort_helper(arr, left, partition_point - 1)
        quicksort_helper(arr, partition_point, right)


def partition(arr, left, right, pivot):
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left


if __name__ == "__main__":
    arr = [2, 1, 4, 0, 0, -2, -4, 20, 5, 3, 3]
    print(arr)
    quicksort(arr)
    print(arr) 
