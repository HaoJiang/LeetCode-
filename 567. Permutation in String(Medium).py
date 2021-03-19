class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter, defaultdict
        window = defaultdict(int)
        need = Counter(s1)
        left = 0
        valid = 0
        for right, val in enumerate(s2):
            if val in need:
                window[val] += 1
                if window[val] == need[val]:
                    valid += 1
            while right - left + 1 >= len(s1):
                if valid == len(need):
                    return True
                d = s2[left]
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                left += 1
        return False

        # s1 = Counter(s1)
        # map = defaultdict(int)
        # required = len(s1)
        # remain = 0
        # left = 0
        # for i in range(len(s2)):
        #     if s2[i] in s1:
        #         map[s2[i]] += 1
        #         if s1[s2[i]] == map[s2[i]]:
        #             remain += 1
        #             if remain == required:
        #                 return True
        #         while map[s2[i]] > s1[s2[i]]:
        #             if map[s2[left]] == s1[s2[left]]:
        #                 remain -= 1
        #             map[s2[left]] -= 1
        #             left += 1
        #     else:
        #         if map:
        #             map.clear()
        #             remain = 0
        #         left = i + 1
        # return False


if __name__ == '__main__':
    print(Solution().checkInclusion(s1="abb", s2="eidobbbbbbbpoaooo"))
