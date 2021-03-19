from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import functools
        @functools.lru_cache(maxsize=None)
        def dfs(total):
            # print(total)
            if total == 0:
                return 0
            if total < 0:
                return -1

            min_coins = float('inf')
            for c in coins:
                cnt = dfs(total - c)
                if cnt == -1:
                    continue
                min_coins = min(cnt + 1, min_coins)
            return min_coins if min_coins != float('inf') else -1
        if amount < 1:
            return 0
        return dfs(amount)

if __name__ == '__main__':
    print(Solution().coinChange(coins = [1, 2, 5], amount = 7))
