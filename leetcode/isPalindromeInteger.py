# Determine whether an integer is a palindrome.
# An integer is a palindrome when it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


test = Solution()

# Test cases
# 1
inp = 123
assert test.isPalindrome(inp) == False

# 2
inp = 90909
assert test.isPalindrome(inp) == True