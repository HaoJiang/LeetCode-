class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        ct = Counter(s)
        for i, v in enumerate(s):
            if ct[v] == 1:
                return i
        return -1
