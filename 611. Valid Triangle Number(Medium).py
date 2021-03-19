from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # total = 0
        #
        # n = len(nums)
        # if n < 3:
        #     return 0
        # for i in range(n - 2):
        #     for j in range(i + 1, n - 1):
        #         for k in range(n - 1, j, -1):
        #             if nums[i] + nums[j] <= nums[k]:
        #                 continue
        #             total += 1
        #
        # return total

        # nums.sort()
        # total = 0
        # for c in range(len(nums) - 1, 1, -1):
        #     a = 0
        #     b = c - 1
        #     while a < b:
        #         if nums[a] + nums[b] > nums[c]:
        #             total += (b - a)
        #             b -= 1
        #         else:
        #             a += 1
        #
        # return total

        nums.sort()
        n = len(nums)
        total = 0
        for a in range(n - 2):
            if not nums[a]:
                continue
            c = a + 2
            for b in range(a + 1, n - 1):
                while c < n and nums[a] + nums[b] > nums[c]:
                    c += 1
                total += (c - b - 1)


if __name__ == '__main__':
    print(Solution().triangleNumber([2, 2, 3, 4]))
