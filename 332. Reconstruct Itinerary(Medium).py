# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
# reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus,
# the itinerary must begin with JFK.
#
#     Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
#     Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
#
#     Input: [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
#     Output: ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
#     Explanation: Another
#     possible
#     reconstruction is ["JFK", "SFO", "ATL", "JFK", "ATL", "SFO"].
#     But
#     it is larger in lexical
#     order.

from typing import List


class Solution:
    def dfs(self, airport):
        while self.adj_list[airport]:
            candidate = self.adj_list[airport].pop()
            self.dfs(candidate)
        self.route.append(airport)

    def findItinerary(self, tickets):
        from collections import defaultdict
        self.route = []
        self.adj_list = defaultdict(list)
        for i, j in tickets:
            self.adj_list[i].append(j)
        for key in self.adj_list:
            self.adj_list[key] = sorted(self.adj_list[key], reverse=True)

        self.dfs("JFK")
        return self.route[::-1]


#         mp = defaultdict(list)
#         for i in tickets:
#             mp[i[0]].append(i[1])
#
#         for i in mp:
#             mp[i].sort()
#
#         self.res = []
#
#         def dfs(root):
#             self.res.append(root)
#
#
# =
#
#         dfs('JFK')
#         return self.res


if __name__ == "__main__":
    print(Solution().findItinerary(
        [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
