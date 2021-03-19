# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
#
# Follow up:
# Could you solve it in linear time?
#
# Example:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # O(n)   time | space O(n)
        res = []

        if not nums or k <= 1:
            return nums

        from collections import deque
        dp = deque()

        for i, v in enumerate(nums):
            while dp and v > nums[dp[-1]]:
                dp.pop()
            dp.append(i)

            if dp[0] <= i - k:
                dp.popleft()

            if i >= k - 1:
                res.append(nums[dp[0]])
        return res

    def maxSilidingwindow(self, nums, k):
        import heapq

        if len(nums) <= 1:
            return nums

        hq = []
        res = []

        for i in range(len(nums)):
            if k - i > 1:
                heapq.heappush(hq, (-nums[i], i))
            else:
                heapq.heappush(hq, (-nums[i], i))
                maxstartidx = i - k + 1
                while hq:
                    val, idx = heapq.heappop(hq)
                    if idx >= maxstartidx:
                        res.append(-val)
                        break
                heapq.heappush(hq, (val, idx))

        return res


print(Solution().maxSilidingwindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
