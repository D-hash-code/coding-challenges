def search(nums: List[int], target: int) -> int:
    def split_and_choose(arr, targ, base):
        n = len(arr)
        if targ > arr[-1]:
            return [], -1
        elif targ >= arr[n // 2]:
            return arr[(n // 2):], base + n // 2
        elif targ > arr[(n // 2) - 1]:
            return [], -1
        elif targ >= arr[0]:
            return arr[:n // 2], base
        else:
            return [], -1

    arr = nums
    base = 0
    while len(arr) > 2:
        arr, new_base = split_and_choose(arr, target, base)
        if new_base == -1:
            return -1
        base = new_base

    if len(arr) <= 2:
        for i, v in enumerate(arr):
            if v == target:
                return base + i
        return -1

    return base
