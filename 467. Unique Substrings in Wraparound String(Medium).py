class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        from collections import defaultdict
        count = 1
        cache = defaultdict(int)
        cache[p[0]] = 1
        for i in range(1, len(p)):
            k = ord(p[i]) - ord(p[i - 1])
            if k == 1 or k == -25:
                count += 1
            else:
                count = 1
            cache[p[i]] = max(count, cache[p[i]])
        return sum(cache.values())


if __name__ == '__main__':
    print(Solution().findSubstringInWraproundString("zab"))
