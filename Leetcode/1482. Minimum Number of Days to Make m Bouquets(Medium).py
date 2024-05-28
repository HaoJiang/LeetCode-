from typing import List


class Solution:
    def mnoftmmb(self, bloomDay: List[List[int]], m, k) -> int:
        left = 1
        right = max(bloomDay)
        if m * k > len(bloomDay):
            return False

        def ispossible(days):
            t = 0
            bouquets = 0
            for i in bloomDay:
                if i <= days:
                    t += 1
                else:
                    bouquets += t // k
                    if bouquets >= m:
                        return True
                    t = 0
            bouquets += t // k
            return bouquets >= m

        while left < right:
            mid = (left + right) // 2
            if ispossible(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    print(Solution().mnoftmmb(bloomDay=[7, 7, 7, 7, 12, 7, 7], m=2, k=3))
