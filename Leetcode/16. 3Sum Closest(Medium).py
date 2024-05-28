# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
#
#
# Constraints:
#
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        closest = sum(nums[:3])
        if closest == target:
            return closest
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    return total
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
        return closest


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    print(Solution().threeSumClosest(nums, target))
