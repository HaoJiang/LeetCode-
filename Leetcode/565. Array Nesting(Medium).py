from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # bottom up
        cache = {}
        def dfs(idx, visited):
            if nums[idx] in visited:
                return 0
            if idx in cache:
                return cache[idx]
            visited.add(nums[idx])
            res = dfs(nums[idx], visited) + 1
            cache[idx] = res
            return res
        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i, set()))
        return res


        # up to down

        # seen = [0] * len(nums)
        # res = 0
        # for idx, val in enumerate(nums):
        #     cnt = 0
        #     while not seen[val]:
        #         seen[nums[val]] = 1
        #         cnt += 1
        #         val = nums[val]
        #
        #     res = max(res, cnt)

if __name__ =='__main__':

    print(Solution().arrayNesting([5,4,0,3,1,6,2]))



