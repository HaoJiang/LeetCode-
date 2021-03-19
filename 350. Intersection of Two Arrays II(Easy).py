from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter

        k = Counter(nums1) & Counter(nums2)
        return [i for i, v in k.items() for j in range(v)]

if __name__ == '__main__':
    print(Solution().intersect([1,2,2,1],
[2,2]))