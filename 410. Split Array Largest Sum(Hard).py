from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        left = max(nums)
        right = sum(nums)

        def ispossible(k):
            total = 0
            cnt = 1
            for i in nums:
                if total + i > k:
                    cnt += 1
                    total = 0
                total += i
            return cnt <= m

        while left < right:
            mid = (left + right) >> 1

            if ispossible(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    print(Solution().splitArray(nums=[7, 2, 5, 10, 8], m=2))
