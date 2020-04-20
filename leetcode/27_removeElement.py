class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            for i, v in enumerate(nums):
                if v == val:
                    nums.pop(i)
        return len(nums)

# Test
#1
a = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
assert(a.removeElement(nums,val) == 5)