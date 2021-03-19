class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        cct = Counter(ransomNote)
        k = cct & Counter(magazine)
        for i, v in cct.items():
            if v != k[i]:
                return False

        return True
