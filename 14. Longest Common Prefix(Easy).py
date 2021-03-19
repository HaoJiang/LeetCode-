from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ''
        if len(strs) < 2:
            return len(strs[0])
        i = 0
        while True:
            for word1, word2 in zip(strs, strs[1:]):
                if i >= min(len(word1), len(word2)) or word1[i] != word2[i]:
                    return word1[:i]
            i += 1


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(strs = ["flower","flow","flight"]))