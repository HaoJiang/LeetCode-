# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.
#
# Example 1:
#
# Input: [[1,1],2,[1,1]]
# Output: 8
# Explanation: Four 1's at depth 1, one 2 at depth 2.
#
# Example 2:
#
# Input: [1,[4,[6]]]
# Output: 17
# Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.

class Solution:
    def nextList_dfs(self, nums):
        self.level = 1
        self.res = 0

        def getmaxLevel(nums, level):
            self.level = max(self.level, level)

            for i in nums:
                if isinstance(i, list):
                    getmaxLevel(i, level + 1)

        def gettotal(nums, level):
            for i in nums:
                if isinstance(i, list):
                    gettotal(i, level - 1)
                else:
                    self.res += i * level

        getmaxLevel(nums, self.level)
        gettotal(nums, self.level)
        return self.res

    def nextList2_bfs(self, nums):
        from collections import deque

        dq = deque()

        self.res = 0
        dq.append(nums)
        level = []
        while dq:
            size = len(dq)
            sum = 0
            for _ in range(size):
                num = dq.popleft()
                for i in num:
                    if isinstance(i, list):
                        dq.append(i)
                    else:
                        sum += i
            level.append(sum)
        n = len(level)
        for i in range(n):
            self.res += level[i] * (n - i)
        return self.res


print(Solution().nextList2_bfs([1, [4, [6]], 2, [3, [3, 4]]]))
