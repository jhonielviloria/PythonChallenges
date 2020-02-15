# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) < 1: return ""
        longest = ""
        for i, letter in enumerate(strs[0]):
            for word in strs:
                if len(word) == i or letter != word[i]:
                    return longest
            longest += letter
        return longest

test = Solution()

# Test case
# 1
inp = ["flower","flow","flight"]
assert test.longestCommonPrefix(inp) == "fl"

# 2
inp = ["dog","racecar","car"]
assert test.longestCommonPrefix(inp) == ""

# Debug
# print(test.longestCommonPrefix((inp)))
