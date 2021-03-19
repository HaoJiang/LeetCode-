# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
#
# Return true if there is a 132 pattern in nums, otherwise, return false.
#
# Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?
#
# Example
# 1:
#
# Input: nums = [1, 2, 3, 4]
# Output: false
# Explanation: There is no
#
# Example 2:
#
# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 3:
            return False

        # i < j < k idx also  [j] > [k] > [i]
        # we want to using decreasing stack   when stack if stack pop means
        # the k < j  we save to k value then find i  when i < k then we found [j] > [k] > [i]
        # because j is biggest in the stack this is monotone decreasing stack

        stack = []
        idxInumber = float('-inf')
        for i in nums[::-1]:
            if i < idxInumber:
                return True
            while stack and i > stack[-1]:
                idxInumber = stack.pop()
            stack.append(i)
        return False


if __name__ == "__main__":
    import  random
    arr = []
    for i in range(10):
        arr.append(random.randint(1, 100))
    print(arr)
    print(Solution().find132pattern(arr))
