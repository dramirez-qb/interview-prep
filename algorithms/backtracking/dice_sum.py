def dice_sum(dice, total):
    '''
    Print all combinations of dice 1-6 that add up to sum
    '''
    chosen = []
    dice_sum_helper(dice, total, 0, chosen)

def dice_sum_helper(dice, total, current_sum, chosen):
    if dice == 0:
        if current_sum == total:
            print(chosen)
    else:
        for i in range(1, 7):
            min = current_sum + i + 1 * (dice - 1)
            max = current_sum + i + 6 * (dice - 1)

            if total >= min and total <= max:
                # choose
                chosen.append(i)
                # explore
                dice_sum_helper(dice - 1, total, current_sum + i, chosen)
                # unchoose
                del chosen[-1]

if __name__ == '__main__':
    dice = int(input().strip())
    total = int(input().strip())
    dice_sum(dice, total)
