from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:

        ##   等差数列    1 2 3    a b c   =  b - a  = c - b      c + a=  2b
        # if len(A) < 3:
        #     return 0
        # dp = len(A) * [0]
        #
        # for i in range(2, len(A)):
        #     if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
        #         dp[i] += dp[i - 1] + 1
        # return sum(dp)

        if len(A) < 3:
            return 0

        a = A[0]
        b = A[1]
        length = 2
        res = 0
        for i in range(2, len(A)):
            if a + A[i] == 2 * b:
                res += length - 1
                length += 1
            else:
                length = 2
            a, b = b, A[i]
        return res


if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices([1, 2, 3, 4, 9, 10, 19]))
