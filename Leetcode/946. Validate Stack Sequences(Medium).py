from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)

        # i = 0
        # pool = set()
        # j = 0
        # flag = True
        # n = len(pushed)
        # while i < n:
        #     if pushed[i] == popped[j] and i not in pool:
        #         pool.add(i)
        #         j += 1
        #         temp = i - 1
        #         if j == len(popped):
        #             return True
        #         while temp >= 0 and temp in pool:
        #             temp -= 1
        #         if temp < 0:
        #             flag = True
        #         else:
        #             if pushed[temp] == popped[j]:
        #                 flag = False
        #                 i = temp
        #                 continue
        #         i += 1
        #     else:
        #         i += 1
        # return False


if __name__ == '__main__':
    print(Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))
