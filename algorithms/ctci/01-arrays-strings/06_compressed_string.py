print('import compressed string')


def compress_string(s):
    compressed = []
    consecutive_count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i] + 1:
            consecutive_count += 1
        else:
            compressed.append(s[i])
            compressed.append(consecutive_count)
            consecutive_count = 1
    compressed.append(s[-1])
    compressed.append(consecutive_count)
    return ''.join(compressed) if len(compressed) < len(s) else s


if __name__ == "__main__":
    s = "aaabbcdeefa"
    print("{} {}".format(s, compress_string(s)))
