from typing import List


class Solution:
    # first solution
    def maxLength(self, arr: List[str]) -> int:
        temp = [""]
        # pre check arr has duplicate
        arr = [i for i in arr if len(set(i)) == len(i)]
        for i in arr:
            # using subset func to list all subset for the arr
            temp += [i + j for j in temp if not (len(set(i)) != len(i) or set(i) & set(j) or len(set(j)) != len(j))]
        print(sorted(temp, key=lambda x: len(x)))
        # using max lamdba check max lenth char in the arr  case we set a empty elemt in the arr
        return len(max(temp, key=len))

    # sec solution   we need using combinenation func or using backtracking check all path then check all elem longest
    # strings
    def maxLength1(self, arr: List[str]) -> int:
        res = []
        ln = len(arr)

        def dfs(index, path):
            res.append(path)
            for idx in range(index, ln):
                dfs(idx + 1, path + arr[idx])
        dfs(0, "")
        print(res)
        return max(res, key=len)


if __name__ == '__main__':
    print(Solution().maxLength1(arr=

                               ["1", "2", "3"]))
