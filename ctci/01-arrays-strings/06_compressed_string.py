print('import compressed string')


def compress_string(s):
    compressed = []
    consecutive_count = 0
    for i, char in enumerate(s):
        consecutive_count += 1
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed.append(s[i])
            compressed.append(str(consecutive_count))
            consecutive_count = 0
    return ''.join(compressed) if len(compressed) > len(s) else s


if __name__ == "__main__":
    s = "aaabbcdeefa"
    print("{} {}".format(s, compress_string(s)))
