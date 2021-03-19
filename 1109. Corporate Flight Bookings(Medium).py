from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = (n + 1) * [0]

        for i, j, k in bookings:
            res[i] += k
            if j < n:
                res[j + 1] -= k

        for i in range(1, n + 1):
            res[i] += res[i - 1]

        return res[1:]

        # res = (n + 1) * [0]
        #
        # for i, j, k in bookings:
        #     for curr in range(i, j + 1):
        #         res[curr] += k
        # return res[1:]


if __name__ == '__main__':
    print(Solution().corpFlightBookings([[3, 3, 5], [1, 3, 20], [1, 2, 15]], n=3))
