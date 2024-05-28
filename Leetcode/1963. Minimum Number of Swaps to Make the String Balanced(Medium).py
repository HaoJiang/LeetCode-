class Solution:
    def minSwaps(self, s: str) -> int:
        # if we saw left bucket we need add 1
        # right side bucket we need -1
        # if cnt < 0 it means we need swap bucket so cnt += 2
        res = 0
        cnt = 0
        for i in s:
            if i == "[":
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    cnt += 2
                    res += 1
        return res


