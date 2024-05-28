# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
#
# Return the length of the longest (contiguous) subarray that contains only 1s.
#
# Example 1:
#
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation:
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
# Example 2:
#
# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation:
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
#
# Note:
#
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] is 0 or 1

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # res = j = 0
        # for i in A:
        #     K = K + i - 1
        #     if K >= 0:
        #         res += 1
        #     else:
        #         K = K - A[j] + 1
        #         j += 1
        # return res
        ### keep window for k >= 0   if k < 0   j++ else i++
        j = 0
        for i in range(len(A)):
            K -= 1 - A[i]
            if K < 0:
                K -= A[j] - 1
                j += 1
        return i - j + 1

        # i = 0
        # maxlen = 0
        # res = 0
        # for j in range(len(A)):
        #     if not A[j]:
        #         while maxlen + K < j - i + 1:
        #             if A[i] == 1:
        #                 maxlen -= 1
        #             i += 1
        #     else:
        #         maxlen += 1
        #     res = max(res, j - i + 1)
        # return res


A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
K = 2
print(Solution().longestOnes(A, K))
