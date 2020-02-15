# The string "PAYPALISHIRING" is written in a zigzag pattern on a
# given number of rows like this: (you may want to display this
# pattern in a fixed font for better legibility)

class Solution:
    def convert(self, s: str, rows: int) -> str:
        if len(s) <= rows or rows == 1: return s
        down = True                     # direction, going down first
        row = -1
        storage = {}
        for i in range(rows):           # initialize a dictionary to store per row
            storage[i] = ""
        for ltr in s:
            if down:
                if row == rows-1:
                    row -= 1
                    down = False
                else:
                    row += 1
            else:
                if row <= 0:
                    row += 1
                    down = True
                else:
                    row -= 1
            storage[row] += ltr
        ans = ''
        for i in range(len(storage)):
            ans += storage[i]
        return ans


test = Solution()
# Test case
# 1
inp_str = "PAYPALISHIRING"
inp_rows = 3
assert test.convert(inp_str, inp_rows) == "PAHNAPLSIIGYIR"

# 2
inp_rows = 2
assert test.convert(inp_str, inp_rows) == "PYAIHRNAPLSIIG"

# Debug
# print(test.convert(inp_str, inp_rows))