def solution(a, b, c, d):
    dice = [a, b, c, d]
    dice_set = list(set(dice))
    cnt = len(dice_set)
    arr = []
    if cnt == 1:
        return 1111 * a
    elif cnt == 2:
        if dice.count(a) == 2:
            return (dice_set[0] + dice_set[1]) * abs(dice_set[0] - dice_set[1])
        else:
            if dice.count(dice_set[0]) == 1:
                return (10 * dice_set[1] + dice_set[0]) ** 2
            else:
                return (10 * dice_set[0] + dice_set[1]) ** 2
    elif cnt == 3:
        for n in dice_set:
            if dice.count(n) == 1:
                arr.append(n)
        return arr[0] * arr[1]
    elif cnt == 4:
        return min(dice_set)