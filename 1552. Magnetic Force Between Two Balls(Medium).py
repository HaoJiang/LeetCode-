from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        left = 1
        right = position[-1] - position[0]

        def ispossible(dis):
            i = 0
            balls = 1
            for j in range(1, len(position)):
                if position[j] - position[i] >= dis:
                    balls += 1
                    i = j
                    if balls >= m:
                        return True
            return balls >= m

        while left < right:
            mid = left + ( right - left + 1) // 2
            print(mid, left, right)
            if ispossible(mid):
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    print(Solution().maxDistance(position=[5,4,3,2,1,1000000000], m=2))
