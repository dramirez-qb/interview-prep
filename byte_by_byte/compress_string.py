print('importing compress string')


def compress_string(s):
    """
    O(s) O(c)
    """
    compressed = []
    consecutive_count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            consecutive_count += 1
        else:
            compressed.append(s[i])
            compressed.append(str(consecutive_count))
            consecutive_count = 1
    compressed.append(s[-1])
    compressed.append(str(consecutive_count))
    return ''.join(compressed) if len(compressed) < len(s) else s

if __name__ == "__main__":
    s = "aaabbcccc"
    print(compress_string(s))
