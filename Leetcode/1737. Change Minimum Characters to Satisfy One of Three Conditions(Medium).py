class Solution:
    def minCharacters(self, a: str, b: str) -> int:

        #######  像是一个  滑轮   从开始 滑到最后   滑动同时 看两侧 移动数量 取最小值   外加数组前缀和

        from collections import defaultdict

        cta = defaultdict(int)
        ctb = defaultdict(int)
        m = len(a)
        n = len(b)
        for i in range(m):
            cta[ord(a[i]) - 97] += 1

        for i in range(n):
            ctb[ord(b[i]) - 97] += 1
        # CONTITION 3    字符 不同或者相同   也就是说 A 和 B 都改成同一个字符 所需要的次数.
        print(ctb.values())
        res = m + n - max(cta.values()) - max(ctb.values())
        #  从基准点 0 开始 到 A - Y   因为 Z 是最大的  两边 如果都是Z 那么到Y RES  = 0

        for i in range(25):
            cta[i + 1] = cta[i]
            ctb[i + 1] = ctb[i]

            # a <= i   b > i
            res = min(res, m - cta[i] + ctb[i])
            res = min(res, n - ctb[i] + cta[i])

        return res


if __name__ == "__main__":
    print(Solution().minCharacters(a="dabadd", b="cza"))
