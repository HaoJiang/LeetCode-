# Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.
#
# Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.
#
# You may return the answer in any order.

# Example 1:
#
# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
# Example 2:
#
# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
# Example 3:
#
# Input: n = 2, k = 0
# Output: [11,22,33,44,55,66,77,88,99]
# Example 4:
#
# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
# Example 5:
#
# Input: n = 2, k = 2
# Output: [13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]

# Constraints:
#
# 2 <= n <= 9
# 0 <= k <= 9

from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        from collections import deque
        dq = deque()
        fator = 10
        for i in range(10 - k):
            if k + i == 0:
                continue
            dq.append((k + i) * fator + i)
            if i != 0 and k + i != i:
                dq.append(i * fator + k + i)
        count = n - 2
        while dq and count:
            size = len(dq)
            for _ in range(size):
                num = dq.popleft()

                lastnum = num % 10
                num *= fator
                if lastnum + k < 10:
                    dq.append(num + lastnum + k)
                if k and lastnum - k > -1:
                    dq.append(num + lastnum - k)
            count -= 1

        return [i for i in dq]


if __name__ == "__main__":
    print(Solution().numsSameConsecDiff(n=3, k=0))
