# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example 1:
#
# Input: 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:
#
# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
# Example 3:
#
# Input: 14
# Output: false
# Explanation: 14 is not ugly since it includes another prime factor 7.


class Solution:
    def isUgly(self, num: int) -> bool:
        # factor 2 3 5

        factor = [2, 3, 5]

        for i in factor:
            while not num % i:
                num //= i
        return num == 1


if __name__ == "__main__":
    print(Solution().isUgly(14))
