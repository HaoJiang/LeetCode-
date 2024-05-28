# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]

# Constraints:
#
# 1 <= n <= 8

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        if not n:
            return

        self.res = []

        def dfs(left, right, path=''):

            if left == right == 0:
                self.res.append(path)
                return
            if right < left:
                return
            if left > 0:
                dfs(left - 1, right, path + "(")
            if right > 0:
                dfs(left, right - 1, path + ')')

        dfs(n, n)

        return self.res


if __name__ == "__main__":

    print(Solution().generateParenthesis(2))
