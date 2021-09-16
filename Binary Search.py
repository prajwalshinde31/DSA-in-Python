def binary_search(hi, lo, condition):

    while hi >= lo:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1

    return -1


def binary_search2(arr, target, high, low):
    mid = (high + low)//2
    mid_num = arr[mid]
    if mid_num == target:
        return mid
    elif mid_num < target:
        return binary_search2(arr, target, high, mid+1)
    elif mid_num > target:
        return binary_search2(arr, target, mid-1, low)


nums = [1, 2, 3, 4, 6, 9, 11, 16, 20]
target = 16
high = len(nums)-1
low = 0
print(binary_search2(nums, target, high, low))




