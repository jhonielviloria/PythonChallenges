# Given a 32-bit signed integer, reverse digits of an integer.

class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        if len(str_x) <= 1: return str_x
        if str_x[0] == "-":
            str_x = "-" + str_x[1::][::-1]
        else:
            str_x = str_x[::-1]
        return str_x


test = Solution()
# Test case
# 1
inp = -10
assert test.reverse(inp) == "-01"

# 2
inp = 123
assert test.reverse(inp) == "321"

# Debug
# print(test.reverse(inp))