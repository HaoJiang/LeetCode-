class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        w1_left = 0
        w1_right = 0
        w2_left = 0
        w2_right = 0
        m = len(word1)
        n = len(word2)
        res = ''
        while w1_right < m and w2_right < n:
            while w1_right < m and w2_right < n and word1[w1_right] == word2[w2_right]:
                w1_right += 1
                w2_right += 1
            if w1_right == m and w2_right == n:
                res += word2[w2_left]
                w2_left += 1
                w2_right = w2_left
                w1_right = w1_left
            elif w1_right == m:
                res += word2[w2_left]
                w2_left += 1
                w2_right = w2_left
                w1_right = w1_left
            elif w2_right == n:
                res += word1[w1_left]
                w1_left += 1
                w1_right = w1_left
                w2_right = w2_left
            elif ord(word1[w1_right]) < ord(word2[w2_right]):
                res += word2[w2_left]
                w2_left += 1
                w2_right = w2_left
                w1_right = w1_left
            else:
                res += word1[w1_left]
                w1_left += 1
                w1_right = w1_left
                w2_right = w2_left
        res += word1[w1_left:] + word2[w2_left:]
        return res

    def largestMerge1(self, word1: str, word2: str) -> str:
        res = ""
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            print(word1[i:])
            if word1[i:] > word2[j:]:  # python 自带的字符串比较功能
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
        if i < len(word1):
            res += word1[i:]
        if j < len(word2):
            res += word2[j:]
        return res



if __name__ == '__main__':
    print(Solution().largestMerge(
        word1="cabaa",
        word2="bcaaa"))
