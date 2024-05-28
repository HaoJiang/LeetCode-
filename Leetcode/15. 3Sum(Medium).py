# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
#
# Example 2:
#
# Input: nums = []
# Output: []
# Example 3:
#
# Input: nums = [0]
# Output: []
#
# Constraints:
#
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Soulutions(object):
    def threeSum(self, nums):
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        res = set()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            j = i + 1
            k = n - 1
            while j < k:
                sm_nums = nums[j] + nums[k] + nums[i]
                if sm_nums == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sm_nums > 0:
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                else:
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
        print (res)
        return res


if __name__ == "__main__":
    nums = [1,-2,-5,-13,-10,-11,0,-12,-11,13,-4,9,8,10,-7,3,-9,-12,-7,8,-2,-12,1,-10,-15,-8,5,14,-7,-8,-8,9,-3,-6,3,-5,-1,-11,-10,3,-13,1,-10,3,-12,-10,-9,-13,-7,-1,10,6,-6,-12,12,-13,-13,-6,-14,-13,-7,-7,4,6,-6,-8,8,8,-4,13,-11,-1,-8,-14,9,-5,-9,7,-3,-1,14,14,13,-7,9,2,-5,12,11,-12,14,-11,-12,3,2,-2,3,-5,-9,14,-14,-13,-10,-7,-12,14,3,-6,-1,8,1,-2,-1,-1,6,-6]
    Soulutions().threeSum(nums)
