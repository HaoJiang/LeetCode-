from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        arr = [weights[0]]
        for i in weights[1:]:
            arr.append(arr[-1] + i)

        left = 1
        right = arr[-1]

        def isPossilble(k):
            count = 0
            total = 0
            for i in weights:
                total += i
                if total > k:
                    count += 1
                    total = i
            return (count + int(total > 0)) <= D

        while left < right:
            mid = (left + right) // 2
            if isPossilble(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    print(Solution().shipWithinDays([1,2,3,1,1],4))
