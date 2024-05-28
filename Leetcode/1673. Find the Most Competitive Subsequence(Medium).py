from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)
        for i in range(n):
            while stack and stack[-1] > nums[i] and n - i - 1 + len(stack) >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(nums[i])

        return stack


if __name__ == "__main__":
    print(Solution().mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2]
,3))