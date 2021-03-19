# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
# Example 2:
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

from collections import defaultdict, deque
def sortedSquares(A):
    answer = deque()
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.appendleft(left * left)
            l += 1
        else:
            answer.appendleft(right * right)
            r -= 1
    return list(answer)


if __name__ == "__main__":
    nums = [-4, -1, 0, 10, 3]
    print(sortedSquares(nums))