class Solution:
    def verifypreorderBST(self, nums):
        if not nums:
            return

        stack = []

        lower = float('-inf')
        for i in nums:
            if i < lower:
                return False
            while stack and i > stack[-1]:
                lower = stack.pop()
            stack.append(i)
        return True


    def verifypreorderBST111(self, nums):

        lower = float('-inf')

        i = -1
        for s in nums:
            if s < lower:
                return False
            while i >= 0 and s > nums[i]:
                lower = nums[i]
                i -= 1
            i += 1
            nums[i] = s



if __name__ == "__main__":
    print(Solution().verifypreorderBST([5, 2, 1, 3, 6]))
