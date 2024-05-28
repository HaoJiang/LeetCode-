from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {}
        for i, v in enumerate(arr):
            mp[v] = i

        for i in pieces:
            if len(i) > 1:
                if i[0] not in mp:
                    return False
                else:
                    t = mp[i[0]]
                    j = 1
                    while j < len(i):
                        if mp.get(i[j], -1) == t + 1:
                            t += 1
                            j += 1
                        else:
                            return False
            else:
                if i[0] not in mp:
                    return False
        return True


if __name__ == "__main__":
    print(Solution().canFormArray(arr=[100, 2, 98, 28, 44, 55, 37], pieces=[[28, 46, 57], [37, 19, 40, 38]]))
