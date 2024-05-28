class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        for idx, citation in enumerate(citations):
            if idx >= citation:
                return idx
        # return len(citations)

    def bucket_Hindex(self, nums):
        n = len(nums)
        backet = [0] * (n + 1)

        for i in nums:
            if i >= n:
                backet[n] += 1
            else:
                backet[i] += 1

        print(backet)
        cur = 0
        for i in range(len(backet) - 1, -1, -1):
            cur += backet[i]
            if cur >= i:
                return i


nums = [1, 0, 1]
print(Solution().hIndex(nums))
