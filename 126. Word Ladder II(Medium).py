# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
#
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
#
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
#
#
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: []
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, word_list: List[str]) -> List[List[str]]:
        word_list = set(word_list)
        if endWord not in word_list:
            return []
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
                if mp[new_word]:
                    graph[word].update(mp[new_word])
            graph[word].discard(word)

        visited = set()
        res = []
        dq = deque()
        dq.append((beginWord, [beginWord]))
        # dq.append((beginWord, 1))
        dis = -1
        while dq:
            start, path = dq.popleft()
            visited.add(start)
            if start == endWord:
                if len(path) > dis > 0:
                    return res
                dis = len(path)
                res.append(path)

            for i in graph[start]:
                if i not in visited:
                    dq.append((i, path + [i]))
        return res


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(Solution().findLadders(beginWord, endWord, wordList))
