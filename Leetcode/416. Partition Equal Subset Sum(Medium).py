from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target, res = divmod(sum(nums), 2)
        if res:
            return False
        import functools
        @functools.lru_cache(maxsize=None)
        def dfs(curr, idx):
            if curr == target:
                return True
            if idx == len(nums):
                return False

            return dfs(curr + nums[idx], idx + 1) or dfs(curr, idx + 1)

        return dfs(0, 0)

        # target, res = divmod(sum(nums), 2)
        # if res: return False
        #
        # sums = {0}  # 存所有子集和
        # for num in nums:
        #     tmp = {s + num for s in sums}  # 遍历已有的子集和，加上num就可以得到更多的子集和
        #     if target in tmp:
        #         return True  # 如果中途达成目标了，就可以返回True了
        #     sums |= tmp  # 加入这一轮得到的子集和
        #
        # return False


if __name__ == "__main__":
    print(Solution().canPartition([1, 5, 11, 5, 4, 4]))
