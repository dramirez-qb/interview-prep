def all_duplicates(arr):
    '''
    Values should be 1 <= x <= len(array)
    Given an array of integers, find all duplicates in the array.
    '''

    if arr is None:
        return None

    dups = set()

    for i, num in enumerate(arr):
        index = abs(num) - 1
        if arr[index] < 0:
            dups.add(abs(arr[i]))
        else:
            arr[index] = - arr[index]

    for i, num in enumerate(arr):
        arr[i] = abs(num)

    return list(dups)

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))

    print(all_duplicates(arr))
