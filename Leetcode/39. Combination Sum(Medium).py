# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
class Solution(object):

    def combinationSumsec(self, candidates, target):
        res = []
        candidates.sort()
        if not candidates:
            return []

        def dfs(index=0, path=[], target=target):

            if target == 0:
                res.append(path)
                return

            for i in range(index, len(candidates)):
                if target - candidates[i] < 0:
                    break
                dfs(i, path + [candidates[i]], target - candidates[i])
        dfs()

        return res

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return
        res = []

        def dfs(index=0, path=[], target=target):
            if target == 0:
                res.append(path)
                return
            elif target < 0:
                return
            else:
                for i in range(index, len(candidates)):
                    if candidates[i] > target:
                        break
                    dfs(i, path + [candidates[i]], target - candidates[i])

        dfs()
        return res


print(Solution().combinationSumsec([2, 3, 6, 7], 7))
