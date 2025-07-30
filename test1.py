def firstMissingPositive(nums):
    nums.sort()
    return nums


nums = [1, 2, 0]
nums2 = [3, 4, -1, 1]
nums3 = [7, 8, 9, 11, 12]
print(firstMissingPositive(nums2))
