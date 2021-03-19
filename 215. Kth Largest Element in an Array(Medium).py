# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        hq = []
        for i in range(len(nums)):
            heapq.heappush(hq, nums[i])
            if len(hq) > k:
                heapq.heappop(hq)
        return heapq.heappop(hq)

    def findkthlargest_quick_sel(self, nums, k):
        import random

        def patations(left, right, pvindex):

            cur = nums[pvindex]
            nums[pvindex], nums[right] = nums[right], nums[pvindex]
            point = left
            for i in range(left, right):  ### [left , right) because right is pvindex
                if nums[i] < cur:
                    nums[i], nums[point] = nums[point], nums[i]
                    point += 1

            nums[right], nums[point] = nums[point], nums[right]

            return point

        def selection(left, right, kth):

            if left == right:
                return nums[left]

            pvindex = random.randint(left, right)

            ck = patations(left, right, pvindex)

            if ck == kth:
                return nums[ck]
            elif ck > kth:
                return selection(left, pvindex - 1, kth)
            else:
                return selection(pvindex + 1, right, kth)

        return selection(0, len(nums) - 1, len(nums) - k)


print(Solution().findkthlargest_quick_sel([3, 2, 1], 2))
