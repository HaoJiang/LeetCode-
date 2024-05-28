class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:

        a, b, c = sorted([a, b, c])
        if a + b <= c:
            return a + b
        else:
            return a + b - (a + b - c - 1) // 2 + 1
