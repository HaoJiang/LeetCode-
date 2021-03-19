from typing import List


class Solution:
    def mnofsdfsdfsdtmmb(self, s, t) -> int:
        m = len(s)
        n = len(t)
        if abs(m - n) > 1:
            return False

        for i in range(min(m, n)):
            if s[i] != t[i]:
                if m == n:
                    return s[i+1:] == t[i+1:]
                elif m > n:
                    return s[i + 1:] == t[i:]
                else:
                    return s[i:] == t[i+1:]
        return True


if __name__ == "__main__":
    print(Solution().mnofsdfsdfsdtmmb(s="ab", t="acb"))
