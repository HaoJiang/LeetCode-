class Solution:
    def countSubstrings(self, s: str) -> int:
        def vaildPail(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count


        total = 0
        for i in range(len(s)):
            total += vaildPail(i, i)
            total += vaildPail(i, i + 1)

        return total

if __name__ == "__main__":

    print(Solution().countSubstrings('aaa'))
