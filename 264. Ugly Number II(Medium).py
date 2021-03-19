# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example:
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq
        # 1 is base  and using bottom up   1 * 2 3 5  cal the nth
        # using heap pop each time a the whole curr min number min heap

        # like dis

        hq = []
        heapq.heappush(hq, 1)
        factor = [2, 3, 5]
        visited = set()
        visited.add(1)
        level = 0
        while hq:
            num = heapq.heappop(hq)
            level += 1
            if level == n:
                return num

            for i in factor:
                k = num
                k *= i
                if k not in visited:
                    heapq.heappush(hq, k)
                    visited.add(k)
        return -1


if __name__ == "__main__":

    print(Solution().nthUglyNumber(1690))


