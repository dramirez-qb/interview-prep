def compress_string(s):
    if s is None:
        return None

    count = 1
    compressed = []

    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            count += 1
        else:
            compressed.append(f'{s[i]}{count}')
            count = 1

    compressed.append(f'{s[-1]}{count}')

    return ''.join(compressed) if len(compressed) < len(s) else s

if __name__ == '__main__':
    s = input().strip()

    print(compress_string(s))
