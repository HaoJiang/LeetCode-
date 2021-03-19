# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
#
# At the end, return the modified image.
#
# Example 1:
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return

        m = len(image)
        n = len(image[0])
        move = ((0, 1), (1, 0), (-1, 0), (0, -1))
        visited = set()
        color = image[sr][sc]

        def dfs(sr, sc):
            visited.add((sr, sc))
            image[sr][sc] = newColor
            for p, q in move:
                new_p = p + sr
                new_q = q + sc
                if m > new_p >= 0 <= new_q < n and (new_p, new_q) not in visited and image[new_p][new_q] == color:
                    dfs(new_p, new_q)
        dfs(sr, sc)

        return image


if __name__ == "__main__":

    print(Solution().floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))