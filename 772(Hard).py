class Solution:
    """
    @param s: the expression string
    @return: the answer
    """

    def calculate(self, s):
        # Write your code here
        num, sign = 0, '+'
        stack = []

        def compute(num, sign):
            if sign == '+':
                stack.append(num)
            if sign == '-':
                stack.append(-num)
            if sign == '*':
                stack.append(stack.pop() * num)
            if sign == "/":
                stack.append(int(stack.pop() / num))

        for c in s + '+':
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/)":
                compute(num, sign)
                if c == ')':
                    num = 0
                    while stack and isinstance(stack[-1], int):
                        num += stack.pop()
                    sign = stack.pop()
                    compute(num, sign)
                num, sign = 0, c
            elif c == '(':
                stack.append(sign)
                sign, num = '+', 0

        return sum(stack)


if __name__ == "__main__":
    print(Solution().calculate("-3*((5-8*2+2/1))"))
