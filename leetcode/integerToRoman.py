# Convert integers to roman numerals


class Solution:
    def intToRoman(self, num: int) -> str:
        conv = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        key_list = list(conv.keys())
        key_list.sort(reverse=True)
        roman = ""

        i = 0
        while i < len(key_list):
            if num >= key_list[i]:
                roman += conv[key_list[i]]
                num -= key_list[i]
            else:
                i += 1

        return roman


test = Solution()

# Test case
# 1
inp = 44
assert test.intToRoman(inp) == "XLIV"

# 2
inp = 999
assert test.intToRoman(inp) == "CMXCIX"

# Debug
# ans = test.intToRoman(inp)
# print(ans)
