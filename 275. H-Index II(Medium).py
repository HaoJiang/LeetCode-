class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # sort n - index return n-index   else return 0
        # because



        # binary search
        # 首先，我们先获取列表的中间元素，即
        # citations[pivot]，它将原始列表分成了两个子列表：citations[0: pivot - 1]
        # 和
        # citations[pivot + 1: n]。
        # 然后比较
        # n - pivot
        # 和
        # citations[pivot]
        # 的值，二分搜索算法分为以下
        # 3
        # 种情况：
        # 若
        # citations[pivot] == n - pivot：则我们找到了想要的元素。
        # 若
        # citations[pivot] < n - pivot：由于我们想要的元素应该大于或等于
        # n - pivot，所以我们应该进一步搜索右边的子列表，即
        # citations[pivot + 1: n]。
        # 若
        # citations[pivot] > n - pivot：我们应该进一步搜索左边的子列表，即
        # citations[0: pivot - 1]。
        #
        # 与典型的二分搜索算法的一个小区别就是，我们返回的结果是
        # n - pivot，而不是所需元素的值。


        # def hIndex(self, citations):
        #     """
        #     :type citations: List[int]
        #     :rtype: int
        #     """
        #     n = len(citations)
        #     left, right = 0, n - 1
        #     while left <= right:
        #         pivot = left + (right - left) // 2
        #         if citations[pivot] == n - pivot:
        #             return n - pivot
        #         elif citations[pivot] < n - pivot:
        #             left = pivot + 1
        #         else:
        #             right = pivot - 1
        #
        #     return n - left

