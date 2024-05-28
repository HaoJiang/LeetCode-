class Solution:
    def ssnnn(self, height, witdh, postion, squirrel, nuts):
        from collections import deque
        # matrix = [witdh * [0] for _ in range(height)]

        # def bfs(visited, startpoint, end):
        #     dq = deque()
        #     dq.append((startpoint[0], startpoint[1], 0))
        #     while dq:
        #         p, q, step = dq.popleft()
        #         visited.add((p, q))
        #         for new_p, new_q in ((p + 1, q), (p, q + 1), (p - 1, q), (p, q - 1)):
        #             if height > new_p >= 0 <= new_q < witdh and (new_p, new_q) not in visited:
        #                 if (new_p, new_q) in end:
        #                     return step + 1, new_p, new_q
        #                 dq.append((new_p, new_q, step + 1))
        #
        # postion = tuple(postion)
        # res = 0
        # endpool = set((i, j) for i, j in nuts)
        # while endpool:
        #     count, i, j = bfs(set(), squirrel, endpool)
        #     res += count
        #     endpool.discard((i, j))
        #     count, i, j = bfs(set(), (i, j), postion)
        #     res += count
        #     squirrel = postion
        # return res

        def distance(start, end):
            return abs(start[0] - end[0]) + abs(start[1] - end[1])

        dis = 0
        d = float('inf')
        for nut in nuts:
            dis += distance(postion, nut) * 2
            d = min(d, distance(squirrel, nut) - distance(nut, postion))
        return dis + d


# x,x,x,x,x,x,x,
# x,x,x,x,x,x,x,
# x,x,x,x,x,x,x,
# x,x,x,x,x,x,x,
# x,x,x,x,x,x,x,

if __name__ == '__main__':
    print(Solution().ssnnn(5,
                           7,
                           [2, 2],
                           [4, 4],
                           [[3, 0], [2, 5]]))
