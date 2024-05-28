class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        t = 0
        k = 1
        i = 0
        while i < len(s):
            if s[i] =='1':
                if k:
                    while i < len(s) and s[i] =='1':
                        i += 1
                    k -= 1
                else:
                    return False
            else:
                i += 1

        return not k

if __name__ == "__main__":
    print(Solution().checkOnesSegment("1001"))