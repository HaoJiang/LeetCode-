# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Note:
#
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
# Example 1:
#
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:
#
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:
#
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation:
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for i in tokens:
            if i in '+-*/':
                # reversed order  1 2   push stack pop  then 2 - 1
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if i == "+":
                    stack.append(num2 + num1)
                elif i == "-":
                    stack.append(num2 - num1)
                elif i == "*":
                    stack.append(num2 * num1)
                else:
                    stack.append(int(num2 / num1))
            else:
                stack.append(i)

        return stack.pop()


if __name__ == "__main__":
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
