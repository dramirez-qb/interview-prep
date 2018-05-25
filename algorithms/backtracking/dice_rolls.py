def dice_rolls(dice):
    '''
    Print all the combinations 1-6 for all dice.
    '''
    chosen = []
    dice_rolls_helper(dice, chosen)

def dice_rolls_helper(dice, chosen):
    if dice == 0:
        print(chosen)
    else:
        for i in range(1, 7):
            # chose
            chosen.append(i)
            # explore
            dice_rolls_helper(dice - 1, chosen)
            # unchoose
            del chosen[-1]

if __name__ == '__main__':
    dice = int(input().strip())
    dice_rolls(dice)
