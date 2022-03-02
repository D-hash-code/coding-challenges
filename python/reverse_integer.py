from math import trunc


def reverse(x: int) -> int:
    if x > 0:
        INT_MAX = 2147483648
        FLIP = False
    else:
        INT_MAX = 2147483647
        x = -x
        FLIP = True

    rev = 0

    while x != 0:

        # pop from x
        pop = x % 10
        x = trunc(x / 10)

        # check for overflow
        if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
            return 0

        # push into rev
        rev = rev * 10 + pop

    if FLIP:
        return -rev
    return rev
