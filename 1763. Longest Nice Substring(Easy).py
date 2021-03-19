class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ''
        map = set(s)

        for idx, val in enumerate(s):
            if val.swapcase() not in map:
                s1 = self.longestNiceSubstring(s[:idx])
                s2 = self.longestNiceSubstring(s[idx + 1:])
                return max(s1, s2, key=len)
        return s


if __name__ == '__main__':
    print(Solution().longestNiceSubstring('aAdsd'))
