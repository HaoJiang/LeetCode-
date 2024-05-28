# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
#
# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
#
# Example 1:
#
# Input: s = "bcabc"
# Output: "abc"
# Example 2:
#
# Input: s = "cbacdcbc"
# Output: "acdb"


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter

        if len(s) < 2:
            return s

        ct = Counter(s)
        last_occ = {c: i for i, c in enumerate(s)}
        print(last_occ)
        stack = []

        for i in s:
            if i not in stack:
                while stack and ord(i) < ord(stack[-1]) and ct[stack[-1]]:
                    stack.pop()
                stack.append(i)
            ct[i] -= 1

        return stack

    def removeduplicate(self, s):
        if len(s) < 2:
            return s

        last_idx = {v: i for i, v in enumerate(s)}
        stack = []
        seen = set()

        for i, v in enumerate(s):
            if v not in seen:
                while stack and v < stack[-1] and i < last_idx[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(v)
                seen.add(v)
        return ''.join(stack)


if __name__ == "__main__":
    print(Solution().removeduplicate('cbacdcbac'))
