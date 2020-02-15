'''Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array which
gives the sum of zero.'''


class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = set()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if not sum:
                    ans.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                elif sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
        return ans


test = Solution()

# Test Cases
# 1
inp = [-1, 0, 1, 2, -1, -4]
assert test.threeSum(inp) == {(-1, 0, 1), (-1, -1, 2)}

# 2
inp = [1, 4, -4, -5, -1, -2, -3, -4]
assert test.threeSum(inp) == {(-5, 1, 4), (-3, -1, 4)}

# 3
inp = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
assert test.threeSum(inp) == {(-4, -2, 6), (-2, -2, 4), (-4, 0, 4), (-4, 1, 3), (-4, 2, 2), (-2, 0, 2)}

# 4
inp = [5, -7, 3, -3, 5, -10, 4, 8, -3, -8, -3, -3, -1, -8, 6, 4, -4, 7, 2, -5, -2, -7, -3, 7, 2, 4, -6, 5]

# 5
assert test.threeSum(inp) == {(-6, 2, 4), (-10, 4, 6), (-7, 3, 4), (-4, -3, 7), (-5, -2, 7), (-3, -1, 4), (-10, 2, 8),
                              (-8, 3, 5), (-7, 2, 5), (-5, -3, 8), (-5, -1, 6), (-10, 5, 5), (-4, -2, 6), (-3, -2, 5),
                              (-2, -1, 3), (-10, 3, 7), (-6, -1, 7), (-4, 2, 2), (-8, 4, 4), (-4, -1, 5), (-8, 2, 6),
                              (-7, -1, 8), (-5, 2, 3), (-3, -3, 6), (-6, -2, 8)}

# 6
inp = [-15, 6, 7, 0, -14, -5, -3, -10, -14, 1, -14, -1, -11, -11, -15, -1, 3, -12, 7, 14, 1, 6, -6, 7, 1, 1, 0, -4, 8,
       7, 2, 1, -2, -6, -14, -9, -3, -1, -12, -2, 7, 11, 4, 12, -14, -4, -4, 4, -1, 10, 3, -14, 1, 12, 0, 10, -9, 8, -9,
       14, -8, 8, 0, -3, 10, -6, 4, -8, 0, -1, -3, -8, -4, 8, 11, -3, -11, -8, 8, 3, 10, -3, -4, -4, -14, 12, 13, -8,
       -3, 12, -8, 4, 5, -1, -14, -8, 8, -3, -9, -15, 12, -5, -7, -15, -12, 11, -11, 14, 11, 12, 3, 6, -6]

# 7
assert test.threeSum(inp) == {(-7, -6, 13), (-10, -2, 12), (-5, 0, 5), (-14, 6, 8), (-3, 1, 2), (-6, 0, 6),
                              (-12, 2, 10), (-8, -5, 13), (-4, 0, 4), (-1, 0, 1), (-15, 1, 14), (-9, -2, 11),
                              (-12, -2, 14), (-10, 3, 7), (-5, 1, 4), (-4, -4, 8), (-14, 7, 7), (-8, 4, 4),
                              (-10, -1, 11), (-7, -5, 12), (-8, -4, 12), (-4, 1, 3), (-11, -2, 13), (-9, 4, 5),
                              (-14, 2, 12), (-3, -3, 6), (-6, -4, 10), (-7, 0, 7), (-6, -5, 11), (-9, -1, 10),
                              (-10, 4, 6), (-4, -3, 7), (-12, -1, 13), (-9, -5, 14), (-7, -4, 11), (-10, 0, 10),
                              (-11, 4, 7), (-5, -3, 8), (-11, 3, 8), (-14, 3, 11), (-8, 0, 8), (-3, -2, 5), (-15, 7, 8),
                              (-12, 4, 8), (-11, -1, 12), (-9, -4, 13), (-12, 0, 12), (-15, 2, 13), (-7, 1, 6),
                              (-5, 2, 3), (-2, -2, 4), (-8, 1, 7), (-6, 2, 4), (-3, -1, 4), (-10, -4, 14), (-5, -2, 7),
                              (-6, 1, 5), (-11, 0, 11), (-12, 5, 7), (-9, 1, 8), (-15, 3, 12), (-7, 2, 5), (-4, -2, 6),
                              (-2, -1, 3), (-10, -3, 13), (-7, -3, 10), (-11, 1, 10), (-11, 5, 6), (0, 0, 0),
                              (-8, 2, 6), (-14, 4, 10), (-8, -3, 11), (-6, -2, 8), (-12, 1, 11), (-9, -3, 12),
                              (-7, 3, 4), (-2, 0, 2), (-1, -1, 2), (-10, 2, 8), (-8, 3, 5), (-5, -1, 6), (-12, 6, 6),
                              (-6, 3, 3), (-5, -5, 10), (-11, -3, 14), (-6, -1, 7), (-14, 1, 13), (-9, 3, 6),
                              (-8, -6, 14), (-8, -2, 10), (-3, 0, 3), (-14, 0, 14), (-15, 5, 10), (-9, 2, 7),
                              (-15, 4, 11), (-4, -1, 5), (-6, -6, 12), (-7, -1, 8), (-2, 1, 1)}

# Debug
# ans = test.threeSum(inp)
# print(ans)