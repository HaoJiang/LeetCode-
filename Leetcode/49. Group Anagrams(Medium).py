from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        map = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord('a')] += 1
            map[tuple(count)].append(i)

        print(map)

if __name__ == '__main__':
    print(Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))

