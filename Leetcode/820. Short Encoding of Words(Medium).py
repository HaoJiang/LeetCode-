from typing import List


class TrieNode:
    def __init__(self):
        from collections import defaultdict
        self.children = defaultdict(Trie)


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ends = []

    def insert(self, word):
        root = self.root
        for char in word:
            root = root.children[char]

        self.ends.append((root, len(word) + 1))


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word[::-1])

        return sum(depth for node, depth in trie.ends if not len(node.children))

# s = set(words)
#
# for word in words:
#     for i in range(1, len(word)):
#         s.discard(word[i:])
# return sum(len(i) + 1 for i in words)
