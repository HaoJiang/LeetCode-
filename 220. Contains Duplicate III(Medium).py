from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i, v in enumerate(nums):
            rg = i + k + 1
            for j in range(i + 1, rg if rg <= len(nums) else len(nums)):
                if abs(nums[j] - nums[i]) <= t:
                    return True

    def containsNearbyAlmostDuplicate1(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or k < 0:
            return False
        all_buckets = {}
        bucket_size = t + 1  # 桶的大小设成t+1更加方便
        for i in range(len(nums)):
            bucket_num = nums[i] // bucket_size  # 放入哪个桶

            if bucket_num in all_buckets:  # 桶中已经有元素了
                return True

            all_buckets[bucket_num] = nums[i]  # 把nums[i]放入桶中

            if (bucket_num - 1) in all_buckets and abs(all_buckets[bucket_num - 1] - nums[i]) <= t:  # 检查前一个桶
                return True

            if (bucket_num + 1) in all_buckets and abs(all_buckets[bucket_num + 1] - nums[i]) <= t:  # 检查后一个桶
                return True

            # 如果不构成返回条件，那么当i >= k 的时候就要删除旧桶了，以维持桶中的元素索引跟下一个i+1索引只差不超过k
            if i >= k:
                all_buckets.pop(nums[i - k] // bucket_size)

        return False


if __name__ == '__main__':
    print(Solution().containsNearbyAlmostDuplicate1(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))
