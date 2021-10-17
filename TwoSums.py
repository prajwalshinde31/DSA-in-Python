class Solution:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]


def two_sum(nums, target):

    for i in range(1, len(nums)):
        temp = nums[i]
        diff = target - temp

        if diff in nums:
            return [i, nums.index(diff)]

        else:
            return 'Target not found'


lst = [i for i in range(11)]
targ = 0
print(two_sum(lst, targ))
