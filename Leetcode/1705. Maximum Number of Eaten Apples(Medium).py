# There is a special kind of apple tree that grows apples every day for n days. On the ith day, the tree grows apples[i] apples that will rot after days[i] days, that is on day i + days[i] the apples will be rotten and cannot be eaten. On some days, the apple tree does not grow any apples, which are denoted by apples[i] == 0 and days[i] == 0.
#
# You decided to eat at most one apple a day (to keep the doctors away). Note that you can keep eating after the first n days.
#
# Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.
#
#
# Example 1:
#
# Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
# Output: 7
# Explanation: You can eat 7 apples:
# - On the first day, you eat an apple that grew on the first day.
# - On the second day, you eat an apple that grew on the second day.
# - On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot.
# - On the fourth to the seventh days, you eat apples that grew on the fourth day
#
#
# Example 2:
#
# Input: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
# Output: 5
# Explanation: You can eat 5 apples:
# - On the first to the third day you eat apples that grew on the first day.
# - Do nothing on the fouth and fifth days.
# - On the sixth and seventh days you eat apples that grew on the sixth day.

from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:

        eat = 0
        remaining_apples = 0
        expired_day = 0

        for day, apple in zip(days, apples):
            expired_day = max(expired_day, day)
            remaining_apples = min(remaining_apples + apple, expired_day)

            if remaining_apples > 0:
                eat += 1
                remaining_apples -= 1
                expired_day -= 1

        return eat + remaining_apples

    def eatenApplesheap(self, apples: List[int], days: List[int]) -> int:

        import heapq

        eat = 0

        curr_day = 0

        hq = []
        while curr_day < len(apples) or hq:
            if curr_day < len(apples) and apples[curr_day]:
                heapq.heappush(hq, [curr_day + days[curr_day], apples[curr_day]])

            while hq and (hq[0][0] <= curr_day or not hq[0][1]):
                heapq.heappop(hq)

            if hq:
                hq[0][1] -= 1
                eat += 1

            curr_day += 1

        return eat

if __name__ =="__main__":
    print(Solution().eatenApplesheap([1],[2]))
