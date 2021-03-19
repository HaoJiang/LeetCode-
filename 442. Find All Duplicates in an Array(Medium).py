from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            t = abs(nums[i]) - 1
            if nums[t] < 0:
                res.append(t + 1)
            else:
                nums[t] = -nums[t]

        return res



if __name__ == "__main__":

    print(Solution().findDuplicates([1,3,2,5,6,7,4,1]))