from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums
        if r > 1 and c > 1:
            matrix = [c * [0] for _ in range(r)]
        elif c == 1:
            matrix = [c * [0] for _ in range(r)]
        else:
            matrix = [c * [0]]
        for i in range(m * n):
            matrix[i // c][i % c] = nums[i // n][i % n]
        return matrix


if __name__ == '__main__':
    print(Solution().matrixReshape(
        [[1, 2],
         [3, 4]], 4, 1))
