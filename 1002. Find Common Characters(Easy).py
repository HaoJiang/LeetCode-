from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        A = [Counter(i) for i in A]
        curr = A[0]
        for i in A[1:]:
            curr &= i
        return list(curr.elements())


if __name__ == '__main__':
    print(Solution().commonChars(["cool", "loooock", "coook"]))
