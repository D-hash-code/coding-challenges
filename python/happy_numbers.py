def isHappy(n: int) -> bool:
    cycle = [n, sum([int(i) ** 2 for i in str(n)])]
    if cycle[-1] == 1:
        return True
    while len(cycle) == len(set(cycle)):
        cycle.append(sum([int(i) ** 2 for i in str(cycle[-1])]))
        if cycle[-1] == 1:
            return True
    return False
