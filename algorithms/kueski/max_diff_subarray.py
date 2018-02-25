def max_diff_subarray(arr):
    """
    [1, 3, 2] -> 2
           ^
    min_value = 1
    max_diff = 2

    diff = 2 - 1 = 1

    O(n) O(1)
    """

    if len(arr) < 2:
        raise ValueError('Array needs to have a length greater than 1')

    min_value = arr[0]
    max_diff = arr[1] - arr[0]

    if len(arr) > 3:
        for i in range(1, len(arr)):
            diff = arr[i] - min_value

            if diff > max_diff:
                max_diff = diff

            if arr[i] < min_value:
                min_value = arr[i]

    return max_diff


if __name__ == '__main__':
    arr = [2, 3, 1, 7, 8, 6, 3]
    print(max_diff_subarray(arr))
