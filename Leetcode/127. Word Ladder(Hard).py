# Given two words beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Return 0 if there is no such transformation sequence.
#
# Example 1:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.
#
# Example 2:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, word_list: List[str]) -> int:
        word_list = set(word_list)
        if endWord not in word_list:
            return 0
        from collections import defaultdict, deque
        mp = defaultdict(set)
        # tp = defaultdict(set)
        graph = defaultdict(set)
        word_list.add(beginWord)
        for word in word_list:
            for i in range(len(word)):
                new_word = word[:i] + '*' + word[i + 1:]
                mp[new_word].add(word)
                # tp[word].add(new_word)

        for word in word_list:
            for i in range(len(word)):
                new_word = word[:i] + '*' + word[i + 1:]
                graph[word].update(mp[new_word])
            graph[word].discard(word)

        visited = set()

        dq = deque()
        dq.append((beginWord, [beginWord]))

        while dq:
            start, path = dq.popleft()
            visited.add(start)
            if start == endWord:
                return path

            for i in graph[start]:
                if i not in visited:
                    dq.append((i, path + [i]))
        return 0


if __name__ == "__main__":
    print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
