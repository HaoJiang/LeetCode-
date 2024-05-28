class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # pool = 26 * [0]
        # n = len(s)
        # left = 0
        # res = 0
        # right = 0
        # while right < n:
        #     pool[ord(s[right]) - 65] += 1
        #     while max(pool) + k < right - left + 1:
        #         pool[ord(s[left]) - 65] -= 1
        #         left += 1
        #     res = max(res, right - left + 1)
        #     right += 1
        # return res

        from collections import defaultdict
        map = defaultdict(int)

        res = 0
        left = 0
        max_count = 0
        for idx, val in enumerate(s):
            map[val] += 1
            max_count = max(max_count, map[val])
            if max_count + k < idx - left + 1:
                map[s[left]] -= 1
                left += 1
            res = max(res, idx - left + 1)
        return res

if __name__ == '__main__' :
    print(Solution().characterReplacement(s = "AABABBA", k = 1))
