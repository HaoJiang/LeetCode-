from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        from collections import Counter

        def check_in(org, w, n, on):
            for i in range(n - on + 1):
                if org[i:on + i] == w:
                    return True
            return False

        res = 0
        n = len(word)
        ct = Counter(patterns)
        for k in ct:
            on = len(k)
            if on <= n:
                if check_in(word, k, n, on):
                    res += ct[k]
        return res


if __name__ == '__main__':
    print(Solution().numOfStrings(patterns=["a", "abc", "bc", "d"], word="abc"))
