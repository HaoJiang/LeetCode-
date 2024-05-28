from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        prefix = [0] * n
        presum = 0
        count = 0
        for i in range(n):
            prefix[i] += presum
            count += int(boxes[i])
            presum += count
        print(prefix)

        postfix = [0] * n
        postsum = 0
        count = 0
        for i in range(n - 1, -1, -1):
            postfix[i] += postsum
            count += int(boxes[i])
            postsum += count
        return [a + b for a, b in zip(prefix, postfix)]
    # map = {idx for idx, val in enumerate(boxes) if int(val)}
    # ans = len(boxes) * [0]
    #
    # for i in range(len(boxes)):
    #     ans[i] = sum(abs(idx - i) for idx in map)
    # return ans


if __name__ == '__main__':
    print(Solution().minOperations('110'))
