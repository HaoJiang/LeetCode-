# Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array by deleting
# some or no elements without changing the order of the remaining elements.
# For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

# Example 1:
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = n * [1]

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)

    def lengthOfLIS123(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else:
                    j = m
            tails[i] = num
            if j == res: res += 1
        return res

    def lengthOfLIS111111(self, nums: List[int]) -> int:

        arr = [nums[0]]

        for i in nums[1:]:
            if i >= arr[-1]:
                arr.append(i)
            else:
                left = 0
                right = len(arr)
                while left < right:
                    mid = (left + right) // 2
                    if arr[mid] > i:
                        right = mid
                    else:
                        left = mid + 1

                arr[left] = i

        return len(arr)

    from typing import List

    def lengthOfLIS32132342(self, nums: List[int]) -> int:
        size = len(nums)
        # 特判
        if size < 2:
            return size

        # 为了防止后序逻辑发生数组索引越界，先把第 1 个数放进去
        tail = [nums[0]]
        for i in range(1, size):
            # 【逻辑 1】比 tail 数组实际有效的末尾的那个元素还大
            # 先尝试是否可以接在末尾
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue

            # 使用二分查找法，在有序数组 tail 中
            # 找到第 1 个大于等于 nums[i] 的元素，尝试让那个元素更小
            left = 0
            right = len(tail) - 1
            while left < right:
                # 选左中位数不是偶然，而是有原因的，原因请见 LeetCode 第 35 题题解
                # mid = left + (right - left) // 2
                mid = (left + right) >> 1
                if tail[mid] < nums[i]:
                    # 中位数肯定不是要找的数，把它写在分支的前面
                    left = mid + 1
                else:
                    right = mid
            # 走到这里是因为【逻辑 1】的反面，因此一定能找到第 1 个大于等于 nums[i] 的元素，因此无需再单独判断
            tail[left] = nums[i]
        return len(tail)





if __name__ == "__main__":
    print(Solution().lengthOfLIS111111([4, 10, 4, 3, 8, 9]
                                       ))
