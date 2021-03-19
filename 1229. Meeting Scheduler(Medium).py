# 题目描述
# 你是一名行政助理，手里有两位客户的空闲时间表：slots1 和 slots2，以及会议的预计持续时间 duration，请你为他们安排合适的会议时间。
#
# 「会议时间」是两位客户都有空参加，并且持续时间能够满足预计时间 duration 的 最早的时间间隔。
#
# 如果没有满足要求的会议时间，就请返回一个 空数组。
#
# 「空闲时间」的格式是 [start, end]，由开始时间 start 和结束时间 end 组成，表示从 start 开始，到 end 结束。
#
# 题目保证数据有效：同一个人的空闲时间不会出现交叠的情况，也就是说，对于同一个人的两个空闲时间 [start1, end1] 和 [start2, end2]，要么 start1 > end2，要么 start2 > end1。
#
# 样例
# 输入：
# slots1 = [[10,50],[60,120],[140,210]],
# slots2 = [[0,15],[60,70]],
# duration = 8
#
# 输出：[60,68]
# 输入：
# slots1 = [[10,50],[60,120],[140,210]],
# slots2 = [[0,15],[60,70]],
# duration = 12
#
# 输出：[]


#
# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.
#
# If there is no common time slot that satisfies the requirements, return an empty array.
#
# The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.
#
# It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.
#
# Example
# 1:
#
# Input: slots1 = [[10, 50], [60, 120], [140, 210]], slots2 = [[0, 15], [60, 70]], duration = 8
# Output: [60, 68]
# Example
# 2:
#
# Input: slots1 = [[10, 50], [60, 120], [140, 210]], slots2 = [[0, 15], [60, 70]], duration = 12
# Output: []
#
# Constraints:
#
# 1 <= slots1.length, slots2.length <= 10^4
# slots1[i].length, slots2[i].length == 2
# slots1[i][0] < slots1[i][1]
# slots2[i][0] < slots2[i][1]
# 0 <= slots1[i][j], slots2[i][j] <= 10^9
# 1 <= duration <= 10^6

class Solution(object):
    def meetingshedule(self, slots1, slots2, duration):

        i = 0
        j = 0
        slots1.sort()
        slots2.sort()
        while i < len(slots1) and j < len(slots2):

            if slots2[j][0] <= slots1[i][0] < slots2[j][1] or slots2[i][0] <= slots1[j][0] < slots2[i][1]:
                st = max(slots1[i][0], slots2[j][0])
                ed = min(slots1[i][1], slots2[j][1])
                if (ed - st) >= duration:
                    return [st, ed]

            if slots1[i][1] < slots2[j][0]:
                i += 1
            else:
                j += 1

        return []


slots1 = [[10, 50], [60, 120], [140, 210]]
slots2 = [[0, 15], [60, 70]]
duration = 8
print(Solution().meetingshedule(slots1,slots2,duration))
