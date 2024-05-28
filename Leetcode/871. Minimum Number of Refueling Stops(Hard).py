# A car travels from a starting position to a destination which is target miles east of the starting position.
#
# Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.
#
# The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.
#
# When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.
#
# What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.
#
# Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

# Example 1:
#
# Input: target = 1, startFuel = 1, stations = []
# Output: 0
# Explanation: We can reach the target without refueling.
# Example 2:
#
# Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
# Explanation: We can't reach the target (or even the first gas station).
# Example 3:
#
# Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
# Output: 2
# Explanation:
# We start with 10 liters of fuel.
# We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
# Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
# and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
# We made 2 refueling stops along the way, so we return 2.
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        import heapq

        total = 0
        i = 0
        hq = []
        heapq.heappush(hq, -startFuel)
        n = len(stations)
        step = 0
        while hq: #or (i < n and stations[i][0] <= total)
            curr = heapq.heappop(hq)
            total -= curr
            if total >= target:
                return step
            while i < n:
                if stations[i][0] <= total:
                    heapq.heappush(hq, -stations[i][1])
                    i += 1
                else:
                    break
            step += 1

        return -1


if __name__ == "__main__":
    print(Solution().minRefuelStops(  target = 200, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))


