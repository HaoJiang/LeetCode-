from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.isWord = True
        node.word = word

    def find(self, word):

        node = self.root

        for c in word:
            node = node.children.get(c)
            if not node:
                return None
        return node


DIRECTIONS = ((0, 1), (1, 0), (-1, 0), (0, -1))


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def dfs(visited, i, j, node):
            if not node:
                return False

            if node.isWord:
                self.res.add(node.word)

            for p, q in DIRECTIONS:
                new_p = p + i
                new_q = q + j

                if m > new_p >= 0 <= new_q < n and (new_p, new_q) not in visited:
                    visited.add((new_p, new_q))
                    dfs(visited, new_p, new_q, node.children.get(board[new_p][new_q]))
                    visited.discard((new_p, new_q))

        if not board:
            return []
        mp = Trie()
        for word in words:
            mp.insert(word)

        self.res = set()

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                dfs(set([(i, j)]), i, j, mp.root.children.get(board[i][j]))

        return self.res


# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         from collections import defaultdict, deque
#
#         prefix = set()
#         word_set = set(words)
#         for word in words:
#             for i in range(len(word)):
#                 prefix.add(word[:i + 1])
#         move = ((0, 1), (1, 0), (-1, 0), (0, -1))
#         self.res = set()
#         m = len(board)
#         n = len(board[0])
#
#         def dfs(prefix, word_set, path, i, j, visited):
#             if path not in prefix:
#                 return
#             if path in word_set:
#                 self.res.add(path)
#             for p, q in move:
#                 _p = p + i
#                 _q = q + j
#                 if m > _p >= 0 <= _q < n and (_p, _q) not in visited:
#                     visited.add((_p, _q))
#                     dfs(prefix, word_set, path + board[_p][_q], _p, _q, visited)
#                     visited.discard((_p, _q))
#
#         for i in range(m):
#             for j in range(n):
#                 visited = set()
#                 visited.add((i, j))
#                 dfs(prefix, word_set, board[i][j], i, j, visited)
#
#         return self.res

# def dfs(i, j, path, idx, visited):
#     visited.add((i, j))
#     if path in self.mp[path[0]]:
#         self.res.append(path)
#         self.mp[path[0]].discard(path)
#     if not self.mp[path[0]]:
#         del self.mp[path[0]]
#
#
#     for p, q in move:
#         new_p = p + i
#         new_q = q + j
#         if m > new_p >= 0 <= new_q < n and (new_p, new_q) not in visited:
#             for t in self.mp[path[0]]:
#                 if t[idx] == board[new_p][new_q]:
#                     dfs(new_p, new_q, path + board[new_p][new_q], idx + 1, visited)
#
#
# self.res = []
#
# self.mp = defaultdict(set)
# for i in words:
#     self.mp[i[0]].add(i)
# m = len(board)
# n = len(board[0])
# move = ((0, 1), (1, 0), (-1, 0), (0, -1))
# for i in range(m):
#     for j in range(n):
#         if board[i][j] in self.mp:
#             dfs(i, j, board[i][j], 1, set())
#
# return self.res


if __name__ == "__main__":
    print(Solution().findWords(
        board=[['a', 'a']],
        words=["aaa"]))
