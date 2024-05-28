class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        from collections import defaultdict
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        if len(s) == 1:
            return True


        return True


if __name__ == "__main__":

    print(Solution().wordPattern(pattern = "abba", s = "dog cat cat fish"))