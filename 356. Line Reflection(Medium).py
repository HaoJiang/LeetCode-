from typing import List


class Solution:
    def lref(self, matrix):
        map = set()
        x_left = float('inf')
        x_right = float('-inf')
        for x, y in matrix:
            x_left = min(x, x_left)
            x_right = max(x, x_right)
            map.add((x, y))
        mid = x_left + x_right
        for x, y in matrix:
            if (mid - x, y) not in map:
                return False
        return True
