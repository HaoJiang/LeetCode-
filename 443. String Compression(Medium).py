from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        pos = 0
        i = 0
        n = len(chars)
        while i < n:
            j = i + 1
            while j < n and chars[i] == chars[j]:
                j += 1
            if j - i > 1:
                chars[pos] = chars[i]
                pos += 1
                for number in str(j - i):
                    chars[pos] = number
                    pos += 1
            else:
                chars[pos] = chars[i]
                pos += 1
            i = j
        return pos


if __name__ == '__main__':
    print(Solution().compress(["x", "7", "7", "2", "2", "2", "f"]))
