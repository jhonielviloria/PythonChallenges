# Convert Roman numerals to Integer


class Solution:
    def romanToInt(self, s: str) -> int:
        conv = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        sum = 0
        for i, ltr in enumerate(s):
            if i+1 < len(s):
                if conv[ltr] >= conv[s[i+1]]:
                    sum += conv[ltr]
                else:
                    sum -= conv[ltr]
            else:
                sum += conv[ltr]
        return sum


test = Solution()

# Test case
# 1
inp = "CMXCIX"
assert test.romanToInt(inp) == 999

# 2
inp = "IX"
assert test.romanToInt(inp) == 9

# 3
inp = "LV"
assert test.romanToInt(inp) == 55

# Debug
# print(test.romanToInt(inp))
