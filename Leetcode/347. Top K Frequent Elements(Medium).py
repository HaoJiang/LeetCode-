# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]


class Solution(object):
    def topKFrequent(self, nums, k):
        from collections import Counter
        import heapq as hq
        lookup = Counter(nums)
        res = []
        heap = []
        for num, freq in lookup.items():
            # 如果堆满了（k个元素）
            if len(heap) == k:
                # 弹出最小频率的元组
                if heap[0][0] > freq:
                    hq.heapreplace(heap, (-freq, num))
            else:
                hq.heappush(heap, (-freq, num))
        while heap:
            res.append(hq.heappop(heap)[1])

        return res


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
