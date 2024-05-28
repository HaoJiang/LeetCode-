class Solutions:
    def lengthOfLongestSubstringKDistinct(self, s, k):

        left = 0
        res = 0
        pool = set()

        for right, val in enumerate(s):
            if val in pool:
                while val in pool:
                    if right - left >= k:
                        res += 1
                    pool.discard(s[left])
                    left += 1
            pool.add(val)
        if len(pool) >= k:
            res += len(pool) - k + 1
        return res


if __name__ == '__main__':
    print(Solutions().lengthOfLongestSubstringKDistinct(s="havefunonleetcode", k=1000))
