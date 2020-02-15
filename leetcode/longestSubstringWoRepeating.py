# Given a string, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
    ans = start = curr = 0
    dic = {}
    for i, char in enumerate(s):
        if char in dic and start < dic[char] + 1:
            start = dic[char] + 1
        curr = i - start + 1
        if curr > ans:
            ans = curr
        dic[char] = i
    return (ans)

# Test case

a = ''
b = ' '
c = 'abba'
d = 'abcabcd'

assert (lengthOfLongestSubstring(a) == 0)
assert (lengthOfLongestSubstring(b) == 1)
assert (lengthOfLongestSubstring(c) == 2)
assert (lengthOfLongestSubstring(d) == 4)