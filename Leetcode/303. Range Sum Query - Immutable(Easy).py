from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.num_sum = [0]
        for i in range(len(nums)):
            self.num_sum.append(self.num_sum[-1] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.num_sum[j + 1] - self.num_sum[i]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(2, 3)
print(param_1)
