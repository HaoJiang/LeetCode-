from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = 0
        odd = 1
        n = len(A)
        while even < n and odd < n:
            if not A[even] % 2:
                even += 2
            elif A[odd] % 2:
                odd += 2
            else:
                A[even], A[odd] = A[odd], A[even]
        return A


if __name__ == '__main__':
    print(Solution().sortArrayByParityII([1, 1, 0, 4]))
