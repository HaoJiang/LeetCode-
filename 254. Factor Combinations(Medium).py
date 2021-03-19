# Example
# Example1
#
# Input: 12
# Output:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
# Explanation:
# 2*6 = 12
# 2*2*3 = 12
# 3*4 = 12
#
# Example2
#
# Input: 32
# Output:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]
# Explanation:
# 2*16=32
# 2*2*8=32
# 2*2*2*4=32
# 2*2*2*2*2=32
# 2*4*4=32
# 4*8=32


class Solution:
    """
    @param n: a integer
    @return: return a 2D array
    """

    def getFactors(self, n):
        # write your code here

        # if n % 2 or n <= 2:
        #     return []

        res = []

        def dfs(n=n, number=2, path=[]):
            while number * number <= n:
                if not n % number:
                    res.append(path + [number, n // number])
                    dfs(n // number, number, path + [number])
                number += 1
        dfs()
        return res


print(Solution().getFactors(35))
