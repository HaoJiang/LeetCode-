class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        total = 0
        # x = ab  y = ba
        if x > y:
            x, y, s = y, x, s[::-1]
        stack = []
        i = 0
        k = 1
        while i < len(s):
            if k and s[i] == 'a' and stack and stack[-1] == 'b':
                total += y
                stack.pop()
            elif not k and s[i] == 'b' and stack and stack[-1] == 'a':
                total += x
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
            if k and i == len(s):
                s = stack
                stack = []
                i = 0
                k = 0
        return total


if __name__ == "__main__":
    print(Solution().maximumGain(s="cdbcbbaaabab", x=4, y=5))
