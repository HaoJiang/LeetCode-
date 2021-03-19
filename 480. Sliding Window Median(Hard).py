# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
#
# Examples:
# [2,3,4] , the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#
# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6

# Therefore, return the median sliding window as [1,-1,-1,3,5,6].
#
# Note:
# You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
# Answers within 10^-5 of the actual value will be accepted as correct.

class Solution(object):

    def medianSlidingWindow(self, nums, k):
        from collections import defaultdict
        import heapq
        if not nums or not k:
            return []
        # nums = [1,3,-1,-3,5,3,6,7], and k = 3.
        maxheap = []  # max heap
        minheap = []  # min heap
        for i in range(k):
            if len(maxheap) == len(minheap):
                heapq.heappush(minheap, -heapq.heappushpop(maxheap, -nums[i]))
            else:
                heapq.heappush(maxheap, -heapq.heappushpop(minheap, nums[i]))

        # right now is balance now
        ans = [float(minheap[0])] if k & 1 else [(minheap[0] - maxheap[0]) / 2.0]
        to_remove = defaultdict(int)
        for i in range(k, len(nums)):  # right bound of window
            # we alway push to max heap   because initial min > max(odd) or min = max(even)
            heapq.heappush(maxheap, -heapq.heappushpop(minheap, nums[i]))  # always push to maxheap
            # we need to keep window and found the number which you want to del
            out_num = nums[i - k]
            # !! important this means if the del number > maxheap  means the del number in minheap
            # so if we need to keep balance we need to give a elements to min heap because minheap has a
            # invalid number that's way we need to give a min heap number
            # if <= mean in maxheap that's ok because the previous we push in to the maxheap
            # so it auto balance now
            if out_num > -maxheap[0]:
                heapq.heappush(minheap, -heapq.heappop(maxheap))
            # now we need the use lazy remove put the del number to the hashtable let +1
            to_remove[out_num] += 1
            # so now we need to clean data  we need to check the first for the both heap if we found the
            # del number we just del that because the vaild number we never remove that and we already cal
            # both two heap balance
            while maxheap and to_remove[-maxheap[0]]:
                to_remove[-maxheap[0]] -= 1
                heapq.heappop(maxheap)
            while to_remove[minheap[0]]:
                to_remove[minheap[0]] -= 1
                heapq.heappop(minheap)
            if k % 2:
                ans.append(float(minheap[0]))
            else:
                ans.append((minheap[0] - maxheap[0]) / 2.0)
        return ans

        # def medianSlidingWindow(self, nums, k):
        # import heapq
        # minheap = []
        # maxheap = []
        # res = []
        # # EX: 7 9 1 3  minheap save 7 9 maxheap save -3 -1
        # # so when we get mid we just peek minheap[0] = 7 maxheap[0] = -(-3)
        # for i in range(k):
        #     if len(minheap) == len(maxheap):
        #         heapq.heappush(minheap, (-heapq.heappushpop(maxheap, (-nums[i], i))[0], i))
        #     else:
        #         heapq.heappush(maxheap, (-heapq.heappushpop(minheap, (nums[i], i))[0], i))
        #
        # res.append(minheap[0][0] if 1 & k else (minheap[0][0] - maxheap[0][0]) / 2.0)
        #
        # for i in range(k, len(nums)):
        #     heapq.heappush(minheap, (nums[i], i))
        #
        #     while minheap and minheap[0][1] <= i - k:
        #         heapq.heappop(minheap)
        #     while maxheap and maxheap[0][1] <= i - k:
        #         heapq.heappop(maxheap)


if __name__ == "__main__":
    print(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
