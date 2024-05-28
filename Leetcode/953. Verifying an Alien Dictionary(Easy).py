from typing import List


class Solution:
    def isAlienSorted(self, words, order):
        orders_idx = {v: i for i, v in enumerate(order)}
        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False
            for i, j in zip(w1, w2):
                if i != j:
                    if orders_idx[i] > orders_idx[j]:
                        return False
                    elif orders_idx[i] < orders_idx[j]:
                        break
        return True


if __name__ == '__main__':
    print(Solution().isAlienSorted(["hello", "leetcode", "leetrtcode", "leettretertrecode"],
                                   "hlabcdefgijkmnopqrstuvwxyz"))
