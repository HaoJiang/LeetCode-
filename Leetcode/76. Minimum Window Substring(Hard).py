# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"

#
# Note:
#
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter, defaultdict
        t = Counter(t)
        required = len(t)
        remaining = 0
        j = 0
        map = defaultdict(int)
        res = float('inf'), 0, 0
        for idx, val in enumerate(s):
            map[val] += 1
            if val in t and t[val] == map[val]:
                remaining += 1
                while j <= idx and remaining == required:
                    if idx - j + 1 < res[0]:
                        res = (idx - j + 1, j, idx)
                    curr = s[j]
                    map[curr] -= 1
                    if curr in t and t[curr] > map[curr]:
                        remaining -= 1
                    j += 1
        return s[res[1]:res[2] + 1] if res[0] < float('inf') else ''


if __name__ == '__main__':
    print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
