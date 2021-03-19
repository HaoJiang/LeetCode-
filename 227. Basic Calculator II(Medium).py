# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
#
# Example 1:
#
# Input: "3+2*2"
# Output: 7
# Example 2:
#
# Input: " 3/2 "
# Output: 1
# Example 3:
#
# Input: " 3+5 / 2 "
# Output: 5


class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = '+'
        stack = []
        for i in s + "+":
            if i.isdigit():
                num = num * 10 + ord(i) - ord('0')
            elif i in '+-*/':
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = i
        return sum(stack)

    def calculate2(self, s):
        num = 0
        res = 0
        sign = 1
        stack = []

        for i in s:
            if i.isdigit():
                num = num * 10 + ord(i) - ord('0')
            elif i in '+-':
                if stack and stack[-1] in '*/':
                    val, oper = stack.pop(), stack.pop()
                    num = val * num if oper == '*' else int(val / num)
                res += num * sign
                num = 0
                sign = 1 if i == "+" else -1
            elif i in '*/':
                if stack and stack[-1] in '*/':
                    val, oper = stack.pop(), stack.pop()
                    num = val * num if oper == "*" else int(val / num)
                stack.extend([num, i])
                num = 0
        return res


if __name__ == "__main__":
    print(Solution().calculate('-3*2 + 1 * 5 - 3'))
