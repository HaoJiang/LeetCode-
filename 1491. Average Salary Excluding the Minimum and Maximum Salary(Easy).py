from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:

        minsalary = float('inf')
        maxsalary = float('-inf')
        total = 0

        for i in salary:
            total += i
            minsalary = min(minsalary, i)
            maxsalary = max(maxsalary, i)
        return (total - maxsalary - minsalary)/ (len(salary) - 2)


if __name__ == '__main__':
    print(Solution().average([6000, 5000, 4000, 3000, 2000, 1000]))
