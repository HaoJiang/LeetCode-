# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
#
# Since the answer may be large, return the answer modulo 10^9 + 7.
#
# Example
# 1:
#
# Input: [3, 1, 2, 4]
# Output: 17
# Explanation: Subarrays
# are[3], [1], [2], [4], [3, 1], [1, 2], [2, 4], [3, 1, 2], [1, 2, 4], [3, 1, 2, 4].
# Minimums
# are
# 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
#
# Note:
#
# 1 <= A.length <= 30000
# 1 <= A[i] <= 30000

class Solution:
    def sumSubarrayMins(self, A):
        # [3, 1, 2, 4]
        #  0  1  0  0  left
        #  0  2  1  0  right
        # (left + 1) * ( right + 1 ) * A[i]
        #  3  6  4  4 = 17
        # O (n*2)
        ans = 0
        for i in range(len(A)):
            left, right = 1, 1
            while i - left >= 0 and A[i - left] > A[i]:
                left += 1

            while right + i < len(A) and A[right + i] >= A[i]:
                right += 1

            ans += left * right * A[i]

            return ans

    def sumSubarrayMins_2(self, A):
        stack = []
        res = temp = 0

        for i, v in enumerate(A):
            count = 1
            while stack and stack[-1][0] >= v:
                k = stack.pop()
                count += k[1]
                temp -= k[0] * k[1]

            stack.append((v, count))

            temp += v * count
            res += temp

            return res % (10 ** 9 + 7)

    def sumSubarrayMins_3(self, A):

        ans = 0
        A = [0] + A + [0]
        stack = []
        for i, a in enumerate(A):
            while stack and A[stack[-1]] > a:
                cur = stack.pop()
                print(A[cur], i - cur, cur - stack[-1], cur , i, stack[-1])
                ans += A[cur] * (i - cur) * (cur - stack[-1])
            stack.append(i)
        return ans % (10 ** 9 + 7)


print(Solution().sumSubarrayMins_3([3, 1, 2, 4]))
