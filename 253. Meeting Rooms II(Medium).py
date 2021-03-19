# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1


class Soultion(object):
    def meetingroom(self, nums):
        start = []
        end = []
        for i in nums:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        print(start, end)
        room = 0
        j = 0
        for i in range(len(start)):
            if start[i] < end[j]:
                room += 1
            else:
                j += 1

        return room

    def meetingroom_heap(self, nums):
        import heapq
        hp = []
        nums.sort()
        heapq.heappush(hp, nums[0])

        for i in range(1, len(nums)):
            if nums[i][0] >= hp[-1][1]:
                heapq.heappop(hp)
            heapq.heappush(hp, nums[i])

        return len(hp)


nums = [[0, 30], [5, 10], [15, 20]]
print(Soultion().meetingroom_heap(nums))
