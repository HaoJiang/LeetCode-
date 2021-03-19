# Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).
#
# After this process, we have some array B.
#
# Return the smallest possible difference between the maximum value of B and the maximum value of B.
#
# Example 1:
#
# Input: A = [1], K = 0
# Output: 0
# Explanation: B = [1]
#
# Example 2:
#
# Input: A = [0,10], K = 2
# Output: 6
# Explanation: B = [2,8]
# Example 3:
#
# Input: A = [1,3,6], K = 3
# Output: 3
# Explanation: B = [4,6,3]
#
# Note:
#
# 1 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 0 <= K <= 10000
from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        small = A[0] - K
        lagre = A[0] + K
        mid = A[0]
        smallest = 0
        if len(A) == 1:
            return 0
        for i in range(1, len(A)):
            a = abs(int(A[i]) - mid)
            b = abs((int(A[i]) + K - small))
            c = abs((int(A[i]) - K) - lagre)
            if (a or b) >= c:
                small = min(small, int(A[i]) - K)
                lagre = max(lagre, int(A[i]) - K)
            elif (a or c) >= b:
                small = min(small, int(A[i]) + K)
                lagre = max(lagre, int(A[i]) + K)
            elif (b or c) >= a:
                small = min(mid, int(A[i]))
                lagre = max(mid, int(A[i]))
            else:
                print(1)
            smallest = lagre - small

        return smallest


if __name__ == "__main__":
    A = [1, 3, 6]
    K = 3
    print(Solution().smallestRangeII(A, K))
