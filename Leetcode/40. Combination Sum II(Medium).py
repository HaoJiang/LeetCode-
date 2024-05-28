# 40. Combination Sum II
# Add to List
#
# Share
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

class Solution(object):

    def combinationsum2sec(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()

        res = []

        def dfs(index=0, path=[], target=target):
            if target == 0:
                if path not in res:
                    res.append(path)
                return

            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    break
                dfs(i + 1, path + [candidates[i]], target - candidates[i])

        dfs()
        return res

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return
        candidates.sort()
        res = []

        def dfs(index=0, path=[], total=target):
            if not total:
                res.append(path)
                return
            if total < 0:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                elif candidates[i] > total:
                    break
                dfs(i + 1, path + [candidates[i]], total - candidates[i])
            print(path, res)

        dfs()
        return res


print(Solution().combinationSum2([2, 5, 2, 1, 2], 5))
