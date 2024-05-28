# Given an array nums of n integers and an integer target, are there elements a, b, c,
# and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Notice that the solution set must not contain duplicate quadruplets.
#
# Example 1:
#
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:
#
# Input: nums = [], target = 0
# Output: []
#
# Constraints:
#
# 0 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109


class Solution(object):

    def fourSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []

        n = len(nums)
        res = []
        nums.sort()
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # if sum(nums[i:i+4]) > target:
            #     break
            for j in range(i+ 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # if (nums[i] + sum(nums[j:j+3])) > target:
                #     break
                left = j + 1
                right = n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1

        return res


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    print(Solution().fourSum1(nums, 0))
