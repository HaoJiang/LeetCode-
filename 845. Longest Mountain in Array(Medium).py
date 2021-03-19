# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
#
# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
#
# (Note that B could be any subarray of A, including the entire array A.)
#
# Given an array A of integers, return the length of the longest mountain.
#
# Return 0 if there is no mountain
#
# Example 1:
#
# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:
#
# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.
#
# Note:
#
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
#
# Follow up:
#
# Can you solve it using only one pass?
# Can you solve it in O(1) space?

class Solution(object):
    def longestMontain33(self, nums):
        if len(nums) < 3:
            return 0
        res = 0
        left_count = 0
        n = len(nums)
        i = 1
        while i < n:
            if res >= n - i + 1:
                return res
            if nums[i] <= nums[i - 1]:
                left_count = 0
                i += 1
                continue
            left_count += 1
            left = i
            right = n - 1
            right_count = 0
            while left < right and nums[left + 1] < nums[left]:
                right_count += 1
                left += 1
            if right_count:
                res = max(right_count + left_count + 1, res)

            if left == i:
                i += 1
            else:
                i = left
        return res

    def longestMontain(self, nums):
        up = down = 0
        res = 0
        for i in range(1, len(nums)):

            if down and nums[i - 1] < nums[i] or nums[i - 1] == nums[i]:
                up = down = 0
            if nums[i] > nums[i - 1]:
                up += 1
            elif nums[i] < nums[i - 1]:
                down += 1
            if down and up:
                res = max(res, up + down + 1)
        return res

    def longestMontain2(self, nums):

        res = 0
        i = 1
        while i < len(nums) - 1:
            ispeak = nums[i - 1] < nums[i] and nums[i] > nums[i + 1]
            if not ispeak:
                i += 1
                continue
            leftIdx = i - 2
            while leftIdx >= 0 and nums[leftIdx] < nums[leftIdx + 1]:
                leftIdx -= 1
            rightIdx = i + 2
            while rightIdx < len(nums) and nums[rightIdx] < nums[rightIdx - 1]:
                rightIdx += 1
            res = max(rightIdx - leftIdx - 1, res)
            i = rightIdx
        return res


if __name__ == "__main__":
    nums = [2, 1, 4, 7, 3, 2, 5]
    print(Solution().longestMontain33(nums))
