# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].


# Example 1:
#
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
#
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
#
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:
#
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"

from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == "]":
                st = ""
                while stack and stack[-1] != "[":
                    st = stack.pop() + st
                stack.pop()
                number = 0
                factor = 1
                while stack and stack[-1].isdigit():
                    base = int(stack.pop())
                    base *= factor
                    factor *= 10
                    number += base
                stack.append(number * st)
            else:
                stack.append(s[i])
        return ''.join(stack)

    def decodeString123(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res


if __name__ == "__main__":
    print(Solution().decodeString(s="2100[leetcode]"))
