# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
#
#
# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
#
#
# Input: n = 33
# Output: 66045
# Constraints:
#
# 1 <= n <= 50

class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [0] + [1] * 5

        for i in range(n):
            for j in range(1, 6):
                dp[j] += dp[j - 1]
        return dp[-1]

        # def cal(n):
        #     if n == 1:
        #         return [0] + 5 * [1]
        #
        #     sm = cal(n - 1)
        #     total = sum(sm)
        #     dp = [0] * 6
        #     for i in range(1, len(sm)):
        #         total -= sm[i - 1]
        #         dp[i] = total
        #
        #     return dp
        #
        # k = cal(n)
        #
        # return sum(k)


if __name__ == "__main__":
    print(Solution().countVowelStrings(3))
