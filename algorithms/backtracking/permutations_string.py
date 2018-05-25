def permute(s):
    permutations = []
    permute_helper(s, '', permutations)
    return permutations

def permute_helper(s, prefix, permutations):
    if len(s) == 0:
        permutations.append(prefix)
    else:
        for i in range(len(s)):
            ch = s[i]
            substr = s[:i] + s[i+1:]
            permute_helper(substr, prefix + ch, permutations)

if __name__ == '__main__':
    s = input().strip()
    print(permute(s))
