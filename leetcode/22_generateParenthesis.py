class Solution(object):
    def generateParenthesis(self, n):
        def combinations(test=[]):
            if len(test) == 2 * n:
                if valid(test):
                    ans.append(''.join(test))
            else:
                test.append('(')
                combinations(test)
                test.pop()
                test.append(')')
                combinations(test)
                test.pop()

        def valid(comb):
            pair = 0
            for c in comb:
                if c == '(':
                    pair += 1
                else:
                    pair -= 1
                if pair < 0:
                    return False
            return pair == 0

        ans = []
        combinations()
        return ans

# Test
a = Solution()

#1
n = 5
print(a.generateParenthesis(n))