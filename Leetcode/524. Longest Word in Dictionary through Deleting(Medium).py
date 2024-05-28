from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))

        for word in d:
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ''


if __name__ == '__main__':
    print(Solution().findLongestWord(s="abpcplea", d=["ale", "apple", "monkey", "plea", "appla"]))
