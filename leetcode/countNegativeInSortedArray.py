# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
# Return the number of negative numbers in grid.


class Solution:
    def countNegatives(self, grid) -> int:
        cnt = 0
        col_len = len(grid)
        if col_len == 0:
            for i in grid:
                if i < 0:
                    cnt += 1
            return cnt
        else:
            row_len = len(grid[0])
            for i in range(col_len):
                if grid[i][0] < 0:
                    cnt += row_len
                    continue
                for j in range(row_len):
                    if grid[i][j] < 0:
                        cnt += row_len - j
                        break
            return cnt

test = Solution()

# Test case
# 1
inp = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
assert test.countNegatives(inp) == 8

# Debug
# print(test.countNegatives(inp))

