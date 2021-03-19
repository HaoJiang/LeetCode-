from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        from collections import Counter, defaultdict
        if not p or not s:
            return []
        length = len(p)
        ct = Counter(p)
        required = len(ct)
        remain = 0
        map = defaultdict(int)
        left = 0
        res = []
        for right in range(len(s)):
            curr = s[right]
            map[curr] += 1
            if curr in ct and map[curr] == ct[curr]:
                remain += 1
            while right - left + 1 >= length:
                if required == remain:
                    res.append(left)
                if map[s[left]] == ct[s[left]]:
                    remain -= 1
                map[s[left]] -= 1
                left += 1
        return res
        # from collections import Counter, defaultdict
        #
        # p = Counter(p)
        # required = len(p)
        # remain = 0
        # left = 0
        # res = []
        # pool = defaultdict(int)
        #
        # for right, val in enumerate(s):
        #     if val in p:
        #         pool[val] += 1
        #         if p[val] == pool[val]:
        #             remain += 1
        #             if remain == required:
        #                 res.append(left)
        #                 pool[s[left]] -= 1
        #                 remain -= 1
        #                 left += 1
        #         elif pool[val] > p[val]:
        #             while pool[val] > p[val]:
        #                 if pool[s[left]] == p[s[left]]:
        #                     remain -= 1
        #                 pool[s[left]] -= 1
        #                 left += 1
        #     else:
        #         left = right + 1
        #         pool.clear()
        #         remain = 0
        # return res


if __name__ == '__main__':
    print(Solution().findAnagrams(s="abaacbabc", p="abc"))
