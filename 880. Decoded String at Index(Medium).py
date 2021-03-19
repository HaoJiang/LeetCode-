# An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:
#
# If the character read is a letter, that letter is written onto the tape.
# If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
# Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.
#
# Input: S = "leet2code3", K = 10
# Output: "o"
# Explanation:
# The decoded string is "leetleetcodeleetleetcodeleetleetcode". The 10th letter in the string is "o".
#
#
# Input: S = "ha22", K = 5
# Output: "h"
# Explanation:
# The decoded string is "hahahaha".  The 5th letter is "h".
#
# Input: S = "a2345678999999999999999", K = 1
# Output: "a"
# Explanation:
# The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".

# Constraints:
#
# 2 <= S.length <= 100
# S will only contain lowercase letters and digits 2 through 9.
# S starts with a letter.
# 1 <= K <= 10^9
# It's guaranteed that K is less than or equal to the length of the decoded string.
# The decoded string is guaranteed to have less than 2^63 letters.
from typing import List


class Solution:
    def decodeAtIndex1(self, S, K):
        size = 0
        # Find size = length of decoded string
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
            print(size)

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1


    def decodeAtIndex(self, S: str, K: int) -> str:
        curridx = 0
        n = len(S)
        for i in range(n):
            if S[i].isdigit():
                curridx *= int(S[i])
            else:
                curridx += 1
            if K <= curridx:
                break
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():

                curridx /= int(S[j])
                K %= curridx
            else:
                if K == curridx or K == 0:
                    return c
                curridx -= 1


if __name__ == "__main__":
    # "aw4eguc6cs"
    # 41
    S = "aw4eguc6cs"
    K = 41
    print(Solution().decodeAtIndex(S, K))
    print(Solution().decodeAtIndex1(S, K))
