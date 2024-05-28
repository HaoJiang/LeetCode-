class Solution:
    def checkValidString(self, s: str) -> bool:

        availble = []
        stack = []

        for idx, val in enumerate(s):
            if val == ")":
                if stack:
                    stack.pop()
                elif availble:
                    availble.pop()
                else:
                    return False
            elif val == '*':
                availble.append(idx)
            else:
                stack.append(idx)

        while stack and availble and stack[-1] < availble[-1]:
            stack.pop()
            availble.pop()
        return not stack

if __name__ == "__main__":
    print(Solution().checkValidString("(*)"))

