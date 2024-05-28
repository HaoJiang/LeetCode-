class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        cnt = 0
        odd = 1
        for i, v in Counter(s).items():
            if v % 2 and odd:
                cnt += 1
                odd -= 1
                v -= 1
            cnt += v if not v % 2 else v - 1
        return cnt


if __name__ == '__main__':
    print(Solution().longestPalindrome((
        "bananas")))
