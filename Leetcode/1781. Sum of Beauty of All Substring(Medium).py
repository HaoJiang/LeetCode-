class Solution:
    def beautySum(self, s: str) -> int:
        from collections import defaultdict
        ans = 0
        for i in range(len(s)):
            cache = defaultdict(int)
            for j in range(i, len(s)):
                cache[s[j]] += 1
                ans += (max(cache.values()) - min(cache.values()))
        return ans
