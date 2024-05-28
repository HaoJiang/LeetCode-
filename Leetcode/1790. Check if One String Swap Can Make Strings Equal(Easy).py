class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        case1 = None
        case2 = None
        cnt = 2
        for a, b in zip(s1, s2):
            if a != b:
                if not cnt:
                    return False
                if case1:
                    if case1 != b or case2 != a:
                        return False
                    cnt -= 1
                else:
                    case1 = a
                    case2 = b
                    cnt -= 1
        if cnt in (2, 0):
            return True
        return False


if __name__ == "__main__":
    print(Solution().areAlmostEqual(s1="kelb", s2="kelb"))
