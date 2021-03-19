# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
#

# Input: height = [4,2,0,3,2,5]
# Output: 9
# n == height.length
# 0 <= n <= 3 * 104
# 0 <= height[i] <= 105

class Solutions(object):

    # Native  O(n * n )  time | space O(1)
    def trapingWater(self, height):
        if len(height) < 3:
            return 0
        res = []
        n = len(height)
        res.append(0)
        for i in range(1, n):
            leftmax = 0
            rightmax = 0
            num = 0
            p = i - 1
            q = i + 1
            while p >= 0:
                leftmax = max(height[p], leftmax)
                p -= 1
            if leftmax > height[i]:
                while q < n:
                    rightmax = max(height[q], rightmax)
                    q += 1
                num = max(min(rightmax, leftmax) - height[i], num)
            res.append(num)

        return sum(res)

    # dp left and right save the max value  space for time

    def trapingWater1(self, height):
        if len(height) < 3:
            return 0

        n = len(height)
        leftmax = n * [0]
        leftmax[0] = height[0]
        for i in range(1, n):
            leftmax[i] = max(leftmax[i - 1], height[i])
        rightmax = n * [0]
        rightmax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightmax[i] = max(rightmax[i + 1], height[i])
        res = 0
        for i in range(len(leftmax)):
            res += min(leftmax[i], rightmax[i]) - height[i]
        print(leftmax, rightmax)
        return res

    # we are using motonitic stack
    # decreasing stack
    def trapingWater2(self, height):
        if len(height) < 3:
            return 0

        res = 0
        stack = []

        for i, v in enumerate(height):
            while stack and v > height[stack[-1]]:
                curr = stack.pop()
                # because we need to compare the stack[-1] if we can found the slot
                if not stack:
                    break
                curheight = min(v, height[stack[-1]]) - height[curr]
                distance = i - stack[-1] - 1  # the index - stack[-1]
                curarea = curheight * distance
                res += curarea
            stack.append(i)
        return res

    def trapingWater3(self, height):
        if len(height) < 3:
            return 0
        left = 0
        right = len(height) - 1
        res = 0
        lmax = rmax = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < lmax:
                    res += lmax - height[left]
                else:
                    lmax = max(lmax, height[left])
                left += 1
            else:
                if height[right] < rmax:
                    res += rmax - height[right]
                else:
                    rmax = max(rmax, height[right])
                right -= 1
        return res


if __name__ == "__main__":
    print(Solutions().trapingWater3([0, 1, 3, 2, 2, 6, 3]))
