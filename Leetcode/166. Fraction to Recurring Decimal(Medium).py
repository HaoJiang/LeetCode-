from typing import List


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = []
        if numerator * denominator < 0:
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        a, remain = divmod(numerator, denominator)
        res.append(str(a))
        if remain:
            res.append('.')
        visited = {}
        while remain:
            if remain in visited:
                idx = visited[remain]
                res.insert(idx, '(')
                res.append(')')
                break
            visited[remain] = len(res)
            remain *= 10
            a, remain = divmod(remain, denominator)
            res.append(str(a))
        return ''.join(res)


if __name__ == '__main__':
    print(Solution().fractionToDecimal(numerator=-2147483648, denominator=1))
