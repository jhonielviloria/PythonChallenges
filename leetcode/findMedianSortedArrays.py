# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

from collections import deque as deq        # use deque for faster popping

def findMedianSortedArrays(nums1, nums2):
        n1 = n3 = deq(nums1)                # n1, n2 as nums1, nums2 converted to deque
        n2 = deq(nums2)                     # n3 as the combination of n1 and n2
        n3.extend(n2)
        n3 = deq(sorted(n3))
        while len(n3) > 2:                  # pop left and right until 1 or 2 is left
            bot = n3.popleft()
            if n1[0] == bot:
                n1.popleft()
            else:
                n2.popleft()
            top = n3.pop()
            if len(n1) > 0 and n1[-1] == top:
                n1.pop()
            elif len(n2) > 0 and n2[-1] == top :
                n2.pop()
        ans = 0
        for i in n3:
            ans += i
        return float(ans)/len(n3)

# Test case
inp_1 = [2,3]
inp_2 = [1]
assert findMedianSortedArrays(inp_1, inp_2) == 2.0