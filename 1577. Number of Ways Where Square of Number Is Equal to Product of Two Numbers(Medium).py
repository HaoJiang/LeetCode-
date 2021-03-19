from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        from collections import Counter

        def getTriplets(map1: Counter, map2: Counter):
            triplets = 0
            for num1, count1 in map1.items():
                square = num1 * num1
                for num2, count2 in map2.items():
                    if square % num2 == 0:
                        num3 = square // num2
                        if num2 == num3:
                            curTriplets = count1 * count2 * (count2 - 1) // 2
                            triplets += curTriplets
                        elif num2 < num3 and num3 in map2:
                            count3 = map2[num3]
                            curTriplets = count1 * count2 * count3
                            triplets += curTriplets
            return triplets

        map1 = Counter(nums1)
        map2 = Counter(nums2)
        return getTriplets(map1, map2) + getTriplets(map2, map1)

if __name__ == '__main__':
    print(Solution().numTriplets(nums1=[7, 4], nums2=[5, 2, 8, 9]))
