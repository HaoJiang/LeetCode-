from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        from collections import Counter
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 > sum2:
            return self.minOperations(nums2, nums1)

        ct = Counter([6 - i for i in nums1] + [i - 1 for i in nums2])
        diff = sum2 - sum1
        ans = 0
        if not diff:
            return 0
        for num in range(5, 0, -1):
            while diff > 0 and ct[num]:
                diff -= num
                ct[num] -= 1
                ans += 1
            if diff <= 0:
                return ans
        return -1


if __name__ == '__main__':
    print(Solution().minOperations([3,3,2,4,2,6,2],
[6,2,6,6,1,1,4,6,4,6,2,5,4,2,1]))
