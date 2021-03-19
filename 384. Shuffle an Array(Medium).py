class Solution:
    from typing import List
    def __init__(self, nums: List[int]):
        self.orgnums = nums[:]
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.orgnums[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        for i in range(len(self.nums)):
            j = random.randint(0, i)
            if i != j:
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        return self.nums


# Your Solution object will be instantiated and called as such:
nums = [-6, 10, 184]
obj = Solution(nums)
param_2 = obj.shuffle()
print(param_2)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)
param_1 = obj.reset()
print(param_1)
param_1 = obj.reset()
print(param_1)
