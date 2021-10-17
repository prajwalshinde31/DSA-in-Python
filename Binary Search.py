<<<<<<< HEAD
from array import array
from math import ceil
from numpy import *


def reverse_binary(nums, high, low, target):
    while low <= high:
        mid = (low + high) // 2

        if target == nums[mid]:
            return mid
        if target == nums[high]:
            return high
        if target == nums[low]:
            return low
        elif target < nums[mid]:
            low = mid + 1
        elif target > nums[mid]:
            high = mid - 1
    return -1


def binary_search(nums, high, low, target):
    while low <= high:
        mid = (low + high) // 2

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1

    return -1


def search(nums, target):

    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    mini = nums.index(min(nums))
    maxi = nums.index(max(nums))
    initial = 0
    final = len(nums) - 1

    if mini > maxi:

        if mini == final and maxi == initial:
            return reverse_binary(nums, mini, maxi, target)
        if nums[maxi] >= target >= nums[initial]:
            return binary_search(nums, maxi, initial, target)
        if nums[mini] <= target <= nums[final]:
            return binary_search(nums, final, mini, target)

    if mini <= maxi:
        return binary_search(nums, maxi, mini, target)
=======
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
>>>>>>> origin/master

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


<<<<<<< HEAD
num = [4,5,6,7,0,1,2]
targ = 6
search(num, targ)

mat = array(
[
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]
)







=======
nums = [1, 2, 3, 4, 6, 9, 11, 16, 20]
target = 16
high = len(nums)-1
low = 0
print(binary_search2(nums, target, high, low))
>>>>>>> origin/master




