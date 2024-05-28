class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """

    def lengthOfLongestSubstringTwoDistinct(self, s):
        # Write your code here

        from collections import defaultdict
        pool = defaultdict(int)
        left = 0
        res = 0
        for right, val in enumerate(s):
            pool[val] += 1
            while len(pool) > 2:
                pool[s[left]] -= 1
                if not pool[s[left]]:
                    del pool[s[left]]
                left += 1
            res = max(res, right - left + 1)
        return res


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstringTwoDistinct('eceba'))
