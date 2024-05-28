from typing import List


class Solution:
    def kWeakestRows(self, pid , ppid, kill) -> List[int]:

        from collections import defaultdict, deque
        map = defaultdict(list)

        for i, j in zip(ppid, pid):
            map[i].append(j)
        dq = deque()
        dq.append(kill)
        ans = set()
        while dq:
            curr = dq.pop()
            ans.add(curr)
            dq.extend(map[curr])
        return ans

if __name__ == '__main__':
    print(Solution().kWeakestRows(pid =  [1, 3, 10, 5],
ppid = [3, 0, 5, 3],
kill = 5))



