# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
#
# Example 2:
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}

        def dfs(s):
            if s in cache:
                return cache[s]
            if not s:
                return []

            patioions = []

            for i in wordDict:
                if not s.startswith(i):
                    continue
                if len(i) == len(s):
                    patioions.append(i)
                else:
                    nxt = dfs(s[len(i):])

                    for nei in nxt:
                        patioions.append(i + ' '+ nei)

            cache[s] = patioions

            return patioions



        return dfs(s)


if __name__ == "__main__":
    print(Solution().wordBreak(s="aaaaaaa", wordDict=["a", "aa", "aaa", "aaaa"]))
