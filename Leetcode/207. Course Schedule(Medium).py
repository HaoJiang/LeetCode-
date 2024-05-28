# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# Input: numCourses = 2, prerequisites = [[1, 0]]
# Output: true
#
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
#
# 3
# [[1,0],[2,1]]

class Solution:
    def canFinish(self, n, pa):

        if n <= 1:
            return True

        from collections import defaultdict, deque

        graph = defaultdict(set)
        indgree = [0] * n
        for i in pa:
            graph[i[1]].add(i[0])
            indgree[i[0]] += 1
        dq = deque()
        dq.extend([i for i in range(n) if not indgree[i]])
        while dq:
            size = len(dq)
            n -= size
            for _ in range(size):
                node = dq.popleft()
                for neighbor in graph[node]:
                    indgree[neighbor] -= 1
                    if not indgree[neighbor]:
                        dq.append(neighbor)

        return n == 0

        # n -= 1


if __name__ == "__main__":
    print(Solution().canFinish(2, [[1, 0]]))
