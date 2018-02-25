def binary_search(arr, x):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid, arr[mid]
        elif x < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1


def binary_search_r(arr, x):
    return binary_search_helper(arr, x, 0, len(arr) - 1)


def binary_search_helper(arr, x, start, end):
    mid = (start + end) // 2
    if arr[mid] == x:
        return mid, arr[mid]
    elif x < arr[mid]:
        return binary_search_helper(arr, x, start, mid - 1)
    else:
        return binary_search_helper(arr, x, mid + 1, end)




if __name__ == "__main__":
    arr = [-2, 1, 1, 5, 3, 7, 9, 0, 0, 4]
    arr.sort()
    print(arr, binary_search(arr, 100))
    print(arr, binary_search_r(arr, 7))
