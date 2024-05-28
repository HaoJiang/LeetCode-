from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        if n <= 1:
            return 0



        from collections import defaultdict, deque

        mp = defaultdict(set)

        for i in range(len(manager)):
            # if manager[i] == -1:
            #     mp[headID].add(headID)
            # else:
            mp[manager[i]].add(i)

        dq = deque()
        dq.append((headID, 0))
        mx = 0
        while dq:
            curr, mins = dq.popleft()
            currmins = informTime[curr] + mins
            mx = max(mx, currmins)
            if curr in mp:
                for i in mp[curr]:
                    dq.append((i, currmins))
        return mx


if __name__ == "__main__":
    print(Solution().numOfMinutes(n=15, headID=0, manager=[-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
                                  informTime=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
