def mergesort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge_halves(left, right)


def merge_halves(left, right):
    if not len(left) or not len(right):
        return left or right

    left_start, right_start = 0, 0
    result = []
    while len(result) < len(left) + len(right):
        if left[left_start] < right[right_start]:
            result.append(left[left_start])
            left_start += 1
        else:
            result.append(right[right_start])
            right_start += 1
        if left_start == len(left) or right_start == len(right):
            result.extend(left[left_start:] or right[right_start:])

    return result


if __name__ == "__main__":
    arr = [-2, 1, 3, 0, 0, 6, 20, 5, 1, -8]
    print(arr, mergesort(arr))
