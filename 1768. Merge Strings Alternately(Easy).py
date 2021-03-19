class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minlen = min(len(word1), len(word2))
        ans = ''
        for a, b in zip(word1, word2):
            ans += a + b
        return ans + (word1[minlen:] or word2[minlen:])


if __name__ == '__main__':
    print(Solution().mergeAlternately(word1="abcd", word2="pq"))
