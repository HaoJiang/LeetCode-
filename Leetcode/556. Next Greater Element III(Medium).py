# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.
#
# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
#
# Example
# 1:
#
# Input: n = 12
# Output: 21
# Example
# 2:
#
# Input: n = 21
# Output: -1
#
# Constraints:
#
# 1 <= n <= 2 ** 31 - 1


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 10:
            return -1
        stack = []
        buf = []
        while n:
            curr = n % 10
            n //= 10
            if stack and stack[-1] > curr and n:
                while stack and stack[-1] > curr:
                    buf.append(stack.pop())
                t = buf.pop()
                stack.append(curr)
                while stack:
                    buf.append(stack.pop())
                buf.append(t)
                nn = 10
                ans = 0
                level = 0
                while buf:
                    ans = ans * nn + buf.pop()
                    level += 1
                return ans if not n else n * (10 ** level) + ans
            stack.append(curr)

        return -1


if __name__ == "__main__":
    print(Solution().nextGreaterElement(1999999999))
