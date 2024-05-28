# Given
# a
# balanced
# parentheses
# string
# S, compute
# the
# score
# of
# the
# string
# based
# on
# the
# following
# rule:
#
# ()
# has
# score
# 1
# AB
# has
# score
# A + B, where
# A and B
# are
# balanced
# parentheses
# strings.
# (A)
# has
# score
# 2 * A, where
# A is a
# balanced
# parentheses
# string.
#
# Example
# 1:
#
# Input: "()"
# Output: 1
# Example
# 2:
#
# Input: "(())"
# Output: 2
# Example
# 3:
#
# Input: "()()"
# Output: 2
# Example
# 4:
#
# Input: "(()(()))"
# Output: 6

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int

        time O(n)  , space O(n)

        we define the (((. ))) . level when we meet ) we cal pre value + max( 2* cur , 1)
        """
        stack = []
        stack.append(0)

        for i in range(len(S)):
            if S[i] == '(':
                stack.append(0)
            else:
                k = stack.pop()
                stack[-1] += max(k * 2, 1)

        return stack.pop()

        # stack = []
        # res = 0
        # k = 0
        # for i in S:
        #     if i == ')' and stack:
        #         while stack[-1] != '(':
        #             k += stack.pop()
        #         if k:
        #             k *= 2
        #         else:
        #             k += 1
        #         stack.pop()
        #     else:
        #         if not stack:
        #             res += k
        #         elif k:
        #             stack.append(k)
        #         stack.append(i)
        #         k = 0
        # res += k
        # return res


print(Solution().scoreOfParentheses('(()(()))'))
