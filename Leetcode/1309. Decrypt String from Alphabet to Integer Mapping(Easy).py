# Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:
#
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
#
# It's guaranteed that a unique mapping will always exist.

# Example 1:
#
# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
#
#
# Example 4:
#
# Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
# Output: "abcdefghijklmnopqrstuvwxyz"


# Constraints:
#
# 1 <= s.length <= 1000
# s[i] only contains digits letters ('0'-'9') and '#' letter.
# s will be valid string such that mapping is always possible.

class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return
        i = len(s) - 1
        res = []

        while i > 0:
            if s[i] == "#":
                res.append(self.alpha(s[i - 2:i]))
                i -= 3
            else:
                res.append(self.alpha(s[i]))
                i -= 1
        return ''.join(res[::-1])

    def freqAlphabets2(self, s):
        if not s:
            return

        i, res = 0, ''
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                res += self.alpha(s[i:i + 2])
                i += 3
            else:
                res += self.alpha(s[i])
                i += 1
        return res

    def alpha(self, num):
        return chr(int(num) + 96)


s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
print(Solution().freqAlphabets2(s))
