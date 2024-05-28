class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import Counter

        ct = Counter(s)
        map = set()
        count = 0
        for idx, val in ct.items():
            if val in map:
                while val in map:
                    count += 1
                    val -= 1
                if val:
                    map.add(val)
            else:
                map.add(val)

        return count


if __name__ == '__main__':
    print(Solution().minDeletions(s="ceabaacb"))
