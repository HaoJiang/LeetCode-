# Given a string, find the length of the longest substring T that contains at most k distinct characters.
#
# Example 1:
#
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:
#
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.

class Solutions:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        from collections import defaultdict

        counter = defaultdict(int)
        left = 0
        longest = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            while len(counter) > k:
                counter[s[left]] -= 1
                if not counter[s[left]]:
                    del counter[s[left]]
                left += 1
            longest = max(longest, right - left + 1)
        return longest


if __name__ == "__main__":
    print(Solutions().lengthOfLongestSubstringKDistinct("eqgkcwGFvjjmxutystqdfhuMblWbylgjxsxgnoh", 16))
