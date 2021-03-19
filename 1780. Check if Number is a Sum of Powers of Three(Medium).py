class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        # 十进制 转 3进制   幂  为3   at most one     不能为2

        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3

        return True