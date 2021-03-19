# two pointer greedy O(MN)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        if not source or not target:
            return 0
        source_set = set(source)
        j = 0
        count = 0
        n = len(source)
        for i, v in enumerate(target):
            if v not in source_set:
                return -1
            while source[j] != v:
                j += 1
                if j == n:
                    j = 0
                    count += 1
            j += 1
            if j == n:
                count += 1
                j = 0

        if j > 0:
            return count + 1
        return count

    def shortestWaybs(self, source: str, target: str) -> int:
        from collections import defaultdict
        if not source or not target:
            return 0
        mp = defaultdict(list)
        for i, v in enumerate(source):
            mp[v].append(i)

        def find_idx(arr, target):
            left = 0
            right = len(arr) - 1
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return arr[left] + 1

        idx = 0
        count = 0
        for ch in target:
            if ch not in mp:
                return -1
            nums = mp[ch]
            if nums[-1] < idx:
                count += 1
                idx = 0
            idx = find_idx(nums, idx)
        if idx > 0:
            return count + 1
        return count

    def shortestWaymap(self, source: str, target: str) -> int:
        mapping = {}
        for i in range(len(source) - 1, -1, -1):
            ch = source[i]
            if i == len(source) - 1:
                mapping[i] = {}
            else:
                mapping[i] = mapping[i + 1].copy()
            mapping[i][ch] = i

        idx = 0
        count = 1
        for ch in target:
            if ch not in mapping[0]:
                return -1
            if idx == len(source) or ch not in mapping[idx]:
                count += 1
                idx = 0
            idx = mapping[idx][ch] + 1

        return count




        # List copy
        # lis = [[-1] * 26 for _ in range(len(source))]
        # for i in range(len(lis) - 1, -1, -1):
        #     if i == len(lis) - 1:
        #         lis[i][ord(source[i]) - ord('a')] = i
        #     else:
        #         lis[i][:] = lis[i + 1]
        #         lis[i][ord(source[i]) - ord('a')] = i


if __name__ == "__main__":
    print(Solution().shortestWaymap(source="abcabba", target="abcabbaabababbabababacccabcbacbacba"))
