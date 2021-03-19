# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
#
# Example 1:
#
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
#
# Example2:
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.


class Solutions(object):
    def giveCandy(self, nums):
        if not nums:
            return []

        res = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            j = i - 1
            if nums[i] > nums[j]:
                res[i] = res[j] + 1
            elif nums[i] == nums[j]:
                continue
            else:
                while j >= 0 and nums[j] > nums[j + 1]:
                    res[j] = max(res[j], res[j + 1] + 1)
        print(res)
        return sum(res)


if __name__ == "__main__":
    nums = [1, 2, 2]
    print(Solutions().giveCandy(nums))
