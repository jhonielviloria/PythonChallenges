# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found. Then, starting from
# this character, takes an optional initial plus or minus sign followed
# by as many numerical chars as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral
# number, which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is
# empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.

class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0: return 0
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "+"]
        symbols = ["-", "+"]
        if len(str) == 1 and str not in digits:
            return 0
        int_min = -2**31
        int_max = 2**31 - 1
        ans = ""
        white = True
        for i in str:
            # while white:
            if white and i == " ":
                continue
            elif white:
                if i not in chars:
                    return 0
                white = False
            if i in chars:
                ans += i
            else:
                break
            if len(ans) > 1 and ans[-1] in symbols:
                ans = ans[0:len(ans)-1]
                break
        try:
            ans = int(ans)
        except ValueError:
            return 0
        if ans > int_max:
            return int_max
        elif ans < int_min:
            return int_min
        else:
            return ans


test = Solution()

# Test case
# 1
inp = "-5-"
assert test.myAtoi(inp) == -5

# 2
inp = "41435fas3"
assert test.myAtoi(inp) == 41435

# 3
inp = "vxeqd-544-"
assert test.myAtoi(inp) == 0

# Debug
# print(test.myAtoi(inp))