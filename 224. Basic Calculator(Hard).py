# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
#
# Example 1:
#
# Input: "1 + 1"
# Output: 2
# Example 2:
#
# Input: " 2-1 + 2 "
# Output: 3
# Example 3:
#
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23

# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.

class Solutions(object):
    # def calculate(self, s: str) -> int:
    #     """
    #     1. Take 3 containers:
    #     num -> to store current num value only
    #     sign -> to store sign value, initially +1
    #     res -> to store sum
    #     When ( comes these containers used for calculate sum of intergers within () brackets.
    #     --------------------
    #     2. When c is + or -
    #     Move num to res, because we need to empty num for next integer value.
    #     set num = 0
    #     sign = update with c
    #     --------------------
    #     3. When c is '('
    #     Here, we need num, res, sign to calculate sum of integers within ()
    #     So, move num and sign to stack => [num, sign]
    #     Now reset - res = 0, num = 0, sign = 1 (default)
    #     --------------------
    #     4. When c is ')' -> 2-(3+4), Here res=3, num=4, sign=1 stack [2, -]
    #     res +=sign*num -> calculate sum for num first, then pop items from stack, res=7
    #     res *=stack.pop() - > Pop sign(+ or -) to multiply with res, res = 7*(-1)
    #     res +=stack.pop() - > Pop integer and add with prev. sum, res = -7 + 2 - 5
    #     --------------------
    #     Simple Example: 2 - 3
    #     Initially res will have 2,i.e. res = 2
    #     then store '-' in sign. it will be used when 3 comes. ie. sign = -1
    #     Now 3 comes => res = res + num*sign
    #     Return statement: res+num*sign => res = 2 + 3(-1) = 2 - 3 = -1
    #     """
    #     num = 0
    #     sign = 1
    #     res = 0
    #     stack = []
    #     for i in range(len(s)):  # iterate till last character
    #         c = s[i]
    #         if c.isdigit():  # process if there is digit
    #             num = num * 10 + int(c)  # for consecutive digits 98 => 9x10 + 8 = 98
    #         elif c in '-+':  # check for - and +
    #             res += num * sign
    #             sign = -1 if c == '-' else 1
    #             num = 0
    #         elif c == '(':
    #             stack.append(res)
    #             stack.append(sign)
    #             res = 0
    #             sign = 1
    #         elif c == ')':
    #             res += sign * num
    #             res *= stack.pop()
    #             res += stack.pop()
    #             num = 0
    #     return res + num * sign

    def calculate2(self, s):
        num = 0
        stack = [1]
        sign = 1
        res = 0

        for ch in s + '+':
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in "-+":
                res += num * stack[-1] * sign
                sign = 1 if ch == '+' else -1
                num = 0
            elif ch == '(':
                stack.append(sign * stack[-1])
                sign = 1
            elif ch == ')':
                res += num * sign * stack[-1]
                num = 0
                stack.pop()

        return res


if __name__ == "__main__":
    print(Solutions().calculate2("-(1+(4+5+2)-3)+(6+8)"))
