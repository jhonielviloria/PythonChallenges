# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 0: return s
        ans = i_ans = start = end = 0
        for i in range(len(s)):
            maxEven = self.maxLen(s, i, i + 1)
            maxOdd = self.maxLen(s, i - 1, i + 1)
            current = max(maxEven, maxOdd)
            if current > ans:
                ans = current
                i_ans = i
                if current == maxEven:
                    start = (i_ans + 1) - ans // 2
                else:
                    start = i_ans - ans // 2
        end = start + ans
        return s[start:end]

    def maxLen(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


test = Solution()

# Test case
# 1
inp = "cscc"
assert test.longestPalindrome(inp) == "csc"

# 2
inp = "abcb"
assert test.longestPalindrome(inp) == "bcb"

# 3
inp = "abcdc"
assert test.longestPalindrome(inp) == "cdc"

# Debug
# print(test.longestPalindrome(inp))
