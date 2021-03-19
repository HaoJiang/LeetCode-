# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        from collections import deque
        dt = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
              "10": ""}
        res = []
        if not digits:
            return res

        dq = deque()
        dq.append("")
        for i in digits:
            for j in range(len(dq)):
                cur_dig = dq.popleft()
                for k in dt[i]:
                    dq.append(cur_dig + k)
        return list(dq)

    def letterCombinationsdfs(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dt = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
              "10": ""}
        res = []

        if not digits:
            return res

        def dfs(index=0, path=""):
            if len(digits) == len(path):
                res.append(path)
                return
            for i in dt[digits[index]]:
                dfs(index + 1, path + i)

        dfs()
        return res

        # self.res = []
        #
        # cache = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        #
        # def dfs(digits, path):
        #     if not digits:
        #         self.res.append(path)
        #         return
        #     for i in cache[digits[0]]:
        #         dfs(digits[1:], path + i)
        #
        # dfs(digits, '')
        # return self.res


print(Solution().letterCombinations('23'))


