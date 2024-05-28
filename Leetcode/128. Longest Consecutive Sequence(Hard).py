from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # map = set(nums)
        # smallest = min(map)
        # res = 0
        # count = 0
        # while map:
        #     map.remove(smallest)
        #     count += 1
        #     smallest += 1
        #     res = max(count, res)
        #     if map and smallest not in map:
        #         smallest = min(map)
        #         count = 0
        # return res

        if not nums:
            return 0
        nums = set(nums)
        longest_range = 1
        while nums:
            left = right = nums.pop()
            while left - 1 in nums:
                nums.remove(left - 1)
                left -= 1
            while right + 1 in nums:
                nums.remove(right + 1)
                right += 1
            longest_range = max(longest_range, right - left + 1)

        return longest_range


if __name__ == '__main__':
    print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
