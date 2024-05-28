# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and ).

#
# Example 1:
#
# Input: "()())()"
# Output: ["()()()", "(())()"]
# Example 2:
#
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# Example 3:
#
# Input: ")("
# Output: [""]

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # from collections import deque
        def isVaildparenthese(lt):
            cnt = 0
            for i in lt:
                if i == "(":
                    cnt += 1
                elif i == ")":
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        dq = set()
        dq.add(s)
        res = []

        while dq:
            valid = list(filter(isVaildparenthese, dq))
            print(valid)

            if valid:
                return valid
            new_dq = set()
            for i in dq:
                for j in range(len(i)):
                    if i[j] == "(" or i[j] == ")":
                        new_dq.add(i[:j] + i[j + 1:])
            dq = new_dq

        return []


if __name__ == "__main__":
    print(Solution().removeInvalidParentheses("()())()"))
