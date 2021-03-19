from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        res = []
        for i, j in queries:
            res.append(arr[j] ^ (arr[i - 1] if i > 0 else 0))
        return res


if __name__ == '__main__':
    print(Solution().xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))
