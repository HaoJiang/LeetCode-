# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
#
# Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.
#
# Example 1:
#
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:
#
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# Example 3:
#
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# 1 <= x <= 109
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        from collections import defaultdict
        total = sum(nums)
        n = len(nums)
        if total == x:
            return n
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + nums[i])
        mp = defaultdict(int)
        mid = total - x
        res = float('-inf')
        for i, v in enumerate(prefix):
            if v - mid in mp:
                res = max(res, i - mp[v - mid])
            else:
                mp[v] = i

        return n - res if res >= 0 else -1

    def minOperationspointer(self, nums: List[int], x: int) -> int:
        mid = sum(nums) - x
        curr = 0
        res = float('-inf')
        start = 0
        for end, number in enumerate(nums):
            curr += number
            while curr > mid and start < end:
                curr -= nums[start]
                start += 1
            if curr == mid:
                res = max(res, end - start + 1)

        return len(nums) - res if res >= 0 else - 1


if __name__ == "__main__":
    print(Solution().minOperationspointer(
        nums = [1,1,4,2,3], x = 5))
