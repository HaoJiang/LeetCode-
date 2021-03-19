class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        left = 0
        pool = set()
        res = 0
        total = 0
        for right, val in enumerate(nums):
            if val in pool:
                while val in pool:
                    total -= nums[left]
                    pool.discard(nums[left])
                    left += 1
            pool.add(val)
            total += val
            res = max(res, total)
        return res


