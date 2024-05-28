class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        curNode = self.root

        for c in word:
            if c not in curNode.children:
                curNode.children[c] = TrieNode()
            curNode = curNode.children[c]

        curNode.isWord = True
        curNode.word = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curNode = self.root

        for c in word:
            curNode = curNode.children.get(c)
            if not curNode:
                return False
        return curNode.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        curNode = self.root

        for c in prefix:
            curNode = curNode.children.get(c)
            if not curNode:
                return False
        return True

    # Your Trie object will be instantiated and called as such:


obj = Trie()
obj.insert('apple')
param_2 = obj.search('apple')
param_3 = obj.startsWith('app')
param_2 = obj.search('app')
# obj.insert('apple')
# param_2 = obj.search('apple')
# obj.insert('apple')
# param_2 = obj.search('apple')
#
#
# ["Trie","insert","search","search","startsWith","insert","search"]
# [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
