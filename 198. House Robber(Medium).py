from typing import List
import cProfile

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)


        print(dp)

cProfile.run(Solution.rob())


