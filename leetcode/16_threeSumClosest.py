class Solution:
    def threeSumClosest(self, nums, target):
        closest = 2**32
        nums.sort()
        prev_i = None
        prev_j = None
        prev_k = None
        for i in range(len(nums)-2):
            if prev_i == nums[i]: continue
            prev_i = nums[i]
            print("i", i)
            for j in range(i+1, len(nums)-1):
                # if prev_j == nums[j]: continue
                # print("j", j)
                # prev_j = nums[j]
                for k in range(j+1, len(nums)):
                    # if prev_k == nums[k]: continue
                    # prev_k = nums[k]
                    sum = nums[i] + nums[j] + nums[k]
                    print("k", k, "sum", sum)
                    if abs(target-sum) > abs(closest-target):
                        continue
                    else:
                        closest = sum
        # return closest

        print(closest)


test = Solution()
# Test cases
# 1
inp_nums = [-1, 2, 1, -4]
inp_target = 1
test.threeSumClosest(inp_nums, inp_target)