def sublists(names):
    '''
    Generate all the sublists from a list of names
    ['Bob', 'Sara']
    ['Bob']
    ['Sara']
    []
    '''
    chosen = []
    sublists_helper(names, chosen)

def sublists_helper(names, chosen):
    if not names:
        print(chosen)
    else:
        name = names[0]
        del names[0]

        # explore once with this person
        chosen.append(name)
        sublists_helper(names, chosen)
        del chosen[-1]

        # explore once without this person
        sublists_helper(names, chosen)

        # unchoose
        names.insert(0, name)

if __name__ == '__main__':
    names = list(input().strip().split())
    sublists(names)
