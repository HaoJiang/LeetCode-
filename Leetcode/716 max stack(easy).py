# Design a max stack that supports push, pop, top, peekMax and popMax.
#
# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
# Example 1:
# MaxStack stack = new MaxStack();
# stack.push(5);
# stack.push(1);
# stack.push(5);
# stack.top(); -> 5
# stack.popMax(); -> 5
# stack.top(); -> 1
# stack.peekMax(); -> 5
# stack.pop(); -> 1
# stack.top(); -> 5


class maxstack:
    def __init__(self):
        self.arr = []
        self.maxstack = []

    def push(self, num):
        self.arr.append(num)
        if self.maxstack and num < self.maxstack[-1]:
            self.maxstack.append(self.maxstack[-1])
        else:
            self.maxstack.append(num)

    def pop(self):
        if not self.arr:
            return
        self.maxstack.pop()
        return self.arr.pop()

    def top(self):
        if not self.arr:
            return
        return self.arr[-1]

    def peekMax(self):
        if not self.maxstack:
            return
        return self.maxstack[-1]

    def popMax(self):
        if not self.maxstack:
            return
        num = self.maxstack[-1]
        buff = []
        while self.top() != num:
            buff.append(self.pop())
        self.pop()

        while buff:
            self.push(buff.pop())
        return


class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """

        res = []
        p = 0
        k = len(target)
        for i in range(1, n + 1):
            if p < k and i == target[p]:
                res.append('Push')
                p += 1
            elif p == k:
                return res
            else:
                res.extend(['Push', 'Pop'])

        return res


if __name__ == "__main__":
    Solution().buildArray([1, 3], 3)
    # a = maxstack()
    # a.push(1)
    # a.push(3)
    # a.push(100)
    # a.push(-1)
    # a.top()
    # a.peekMax()
    # a.pop()
    # a.popMax()
    # a.peekMax()
