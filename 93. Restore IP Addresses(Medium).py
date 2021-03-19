# Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.
#
# A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1"
# are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.


# Example 1:
#
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        if len(s) <= 3:
            return -1

        self.res = []

        def dfs(idx, path):
            if idx == len(s):
                if len(path) == 4:
                    self.res.append(','.join(path))
                return

            if len(path) > 3:
                return
            if s[idx] == '0':
                dfs(idx + 1, path + [s[idx]])
            number = 0
            for i in range(idx, len(s)):
                number = number * 10 + ord(s[i]) - ord('0')
                if 0 < number <= 255:
                    dfs(i + 1, path + [str(number)])
                else:
                    return

        dfs(0, [])

        return self.res


        # self.res = []
        # path = [0] * 4
        #
        # def dfs(level, curr):
        #     if level == 4:
        #         if curr == len(s):
        #             self.res.append('.'.join(str(i) for i in path))
        #         return
        #     if curr == len(s):
        #         return
        #     if s[curr] == "0":
        #         path[level] = 0
        #         dfs(level + 1, curr + 1)
        #
        #     num = 0
        #     for i in range(curr, len(s)):
        #         num = num * 10 + ord(s[i]) - ord("0")
        #         if 0 < num <= 255:
        #             path[level] = num
        #             dfs(level + 1, i + 1)
        #         else:
        #             break
        #
        # dfs(0, 0)

        return self.res


# class Solution:
#     def restoreIpAddresses(self, s: str) -> List[str]:
#         ans = []
#         segments = [0] * 4
#
#         def dfs(segId: int, segStart: int):
#             # 如果找到了 4 段 IP 地址并且遍历完了字符串，那么就是一种答案
#             if segId == 4:
#                 if segStart == len(s):
#                     ipAddr = ".".join(str(seg) for seg in segments)
#                     ans.append(ipAddr)
#                 return
#
#             # 如果还没有找到 4 段 IP 地址就已经遍历完了字符串，那么提前回溯
#             if segStart == len(s):
#                 return
#
#             # 由于不能有前导零，如果当前数字为 0，那么这一段 IP 地址只能为 0
#             if s[segStart] == "0":
#                 segments[segId] = 0
#                 dfs(segId + 1, segStart + 1)
#
#             # 一般情况，枚举每一种可能性并递归
#             addr = 0
#             for segEnd in range(segStart, len(s)):
#                 addr = addr * 10 + ord(s[segEnd]) - ord("0")
#                 if 0 < addr <= 255:
#                     segments[segId] = addr
#                     dfs(segId + 1, segEnd + 1)
#                 else:
#                     break
#
#         dfs(0, 0)
#         return ans


if __name__ == "__main__":
    print(Solution().restoreIpAddresses(s="0000"))
