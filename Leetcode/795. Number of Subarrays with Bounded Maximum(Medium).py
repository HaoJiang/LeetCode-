from typing import List


class Solution:
    def numSubarrayBoundedMax(self, A: List[int], R: int) -> int:
        def notGreater(R):
            ans = cnt = 0
            for a in A:
                if a <= R:
                    cnt += 1
                else:
                    cnt = 0
                ans += cnt
            return ans

        # left = 0
        # res = count = 0
        #
        # for right, x in enumerate(A):
        #     if x >= L and x <= R:
        #         count = right - left + 1
        #     elif x > R:
        #         count = 0
        #         left = right + 1
        #
        #     res += count
        return notGreater(R)


if __name__ == '__main__':
    print(Solution().numSubarrayBoundedMax([1,3,4],
                                           3))
