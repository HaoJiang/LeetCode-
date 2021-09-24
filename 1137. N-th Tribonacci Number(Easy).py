class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        first = 0
        sec = 1
        third = 1
        res = first + sec + third
        for i in range(3, n):
            first, sec, third = sec, third, res
            res = first + sec + third

        return res

if __name__ == "__main__":
    print(Solution().tribonacci(25))
