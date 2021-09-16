def reverse(nums):
    # reverse the elements of an array

    n = len(nums) - 1
    for i in range(len(nums)):
        if i <= n:
            x = nums[i]
            nums[i] = nums[n]
            nums[n] = x
        n = n-1
    return nums

nums = [1,2,3]
print(reverse(nums))
