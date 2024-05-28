# Now, we define a pair (c, d) can follow another pair (a, b)
# if and only if b < c. Chain of pairs can be formed in this fashion.

#
# Example 1:
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        arr = [pairs[0]]
        for i in pairs[1:]:
            if i[0] > arr[-1][1]:
                arr.append(i)
        return len(arr)


if __name__ == "__main__":
    print(Solution().findLongestChain([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]))

