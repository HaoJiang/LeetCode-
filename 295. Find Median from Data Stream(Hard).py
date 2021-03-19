# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
#
# For example,
# [2,3,4], the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.

# Example:
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
# Follow up:
#
# If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initializ
        e your data structure here.
        """
        self.maxheap = []
        self.minheap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.minheap) == len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappushpop(self.minheap, num))
        else:
            heapq.heappush(self.minheap, -heapq.heappushpop(self.maxheap, -num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2
        else:
            return -self.maxheap[0]


if __name__ =="__main__":
    a = MedianFinder()
    a.addNum(5)
    a.addNum(2)
    a.addNum(9)
    a.addNum(14)
    print(a.findMedian())


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
