from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = premax = premin = nums[0]

        for i in nums[1:]:
            currmax = max(premax * i, premin * i, i)
            currmin = min(premax * i, premin * i, i)
            ans = max(currmax, ans)
            premax = currmax
            premin = currmin
        return ans


if __name__ == '__main__':
    print(Solution().maxProduct([2,0, 3,0, -2, 4]))
