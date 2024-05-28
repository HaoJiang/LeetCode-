# # Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.
#
# Example:
#
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
#
#
# Constraints:
#
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        self.res = []

        def dfs(idx, path):
            if len(path) > 1:
                self.res.append(path)
            for i in range(idx, len(nums)):
                print(i, idx, nums[i], path)
                if path and path[-1] > nums[i]:
                    continue
                elif i > idx and nums[i] == nums[i - 1]:
                    continue
                else:
                    dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return self.res


if __name__ == "__main__":
    print(Solution().findSubsequences([4, 6, 5, 7, 7]))
