def permutations(arr):
    results = []
    permutations_helper(arr, 0, results)
    return results


def permutations_helper(arr, start, results):
    if start >= len(arr):
        results.append(arr[:])
    else:
        for i in range(start, len(arr)):
            arr[i], arr[start] = arr[start], arr[i]
            permutations_helper(arr, start + 1, results)
            arr[i], arr[start] = arr[start], arr[i]


if __name__ == '__main__':
    arr = ['ab', 'bb', 'aa']
    for permutation in permutations(arr):
        print(permutation)
