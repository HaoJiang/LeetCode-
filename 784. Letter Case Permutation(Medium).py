from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def recall(S, start):
            res.append(''.join(S))
            for i in range(start, len(S)):
                if S[i].isalpha():
                    S[i] = S[i].swapcase()
                    recall(S, i + 1)
                    S[i] = S[i].swapcase()

        res = []
        S = list(S)
        recall(S, 0)
        return res

if __name__ == '__main__':
    print(Solution().letterCasePermutation(S = "a1b2"))
