# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

class Solution:
    def twoSum(self, nums, target):
        for i, x in enumerate(nums):
            y = target - x
            if y in nums:
                j = nums.index(y)
                if i == j: continue
                return [i, j]


test = Solution()

# Test case
# 1
inp_nums = [3, 2, 4]
inp_target = 6
assert test.twoSum(inp_nums, inp_target) == [1, 2]

#2
inp_nums = [2,7,11,15]
inp_target = 9

assert test.twoSum(inp_nums, inp_target) == [0, 1]

# Debug
# print(test.twoSum(inp_nums, inp_target))
