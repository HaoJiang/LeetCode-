# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#
# Example 1:
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
import time


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        # write your code here
        def dfs(s1, s2, s3, memo):

            if len(s1) + len(s2) != len(s3):
                return False
            if not s1 and not s2 and not s3:
                return True
            if (s1, s2, s3) in memo:
                return memo[s1, s2, s3]
            memo[s1, s2, s3] = \
                (len(s1) > 0 and len(s3) > 0 and s1[0] == s3[0] and dfs(s1[1:], s2, s3[1:], memo)) \
                or (len(s2) > 0 and len(s3) > 0 and s2[0] == s3[0] and dfs(s1, s2[1:], s3[1:], memo))
            # print(memo)
            return memo[s1, s2, s3]

        return dfs(s1, s2, s3, {})

    def isInterleave1(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        dp = [[True for _ in range(c + 1)] for _ in range(r + 1)]
        for i in range(1, r + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, c + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])
        return dp[-1][-1]


s1 = "fdsssssssssssssssssf"
s2 = "sdffdsfds"
s3 = "aaaaaaaaaaaafdsaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacaadca"
start = time.time()
print(Solution().isInterleave1(s1, s2, s3))
end = time.time()
print(end - start)
