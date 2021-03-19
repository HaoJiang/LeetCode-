from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.ans = float('inf')
        toppingCosts.sort()

        def dfs(toppingCosts, target, path):
            if abs(target - path) < abs(target - self.ans):
                self.ans = path
            if path > target:
                return

            for i in range(len(toppingCosts)):
                dfs(toppingCosts[i + 1:], target, path + toppingCosts[i] * 0)
                dfs(toppingCosts[i + 1:], target, path + toppingCosts[i] * 1)
                dfs(toppingCosts[i + 1:], target, path + toppingCosts[i] * 2)

        for base in baseCosts:
            dfs(toppingCosts, target, base)
        return self.ans


if __name__ == '__main__':
    print(Solution().closestCost(baseCosts=[10], toppingCosts=[1], target=1))
