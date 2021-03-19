# There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.
#
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
#
# Your score is the sum of the points of the cards you have taken.
#
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

# Example 1:
#
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1.
# However, choosing the rightmost card first will maximize your total score.
# The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.


# [100,40,17,9,73,75]
# 3
# 248

from typing import List


class Solution:
    def maxScore(self, A: List[int], k: int) -> int:
        n = len(A)
        total = sum(A)
        if n == k:
            return total
        leftMax = sum(A[-k:])
        rightMax = sum(A[:k])

        t = n - k
        bestMin = 0
        currMin = 0
        i = 0
        while i < t:
            bestMin += A[i]
            currMin += A[i]
            i += 1
        j = 0
        while i < n:
            currMin -= A[j] - A[i]
            bestMin = min(bestMin, currMin)
            j += 1
            i += 1
        return max(leftMax, rightMax, total - bestMin)


if __name__ == "__main__":
    print(Solution().maxScore([1,2,3,4,5,6,1], 3))
