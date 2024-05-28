class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].lower() not in vowels:
                left += 1
            elif s[right].lower() not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)


if __name__ == '__main__':
    print(Solution().reverseVowels("leetcode"))
