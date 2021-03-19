# A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
#
# Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.
#
# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
#
# Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.
#
# Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.
#
# Note:
#
# Starting point is assumed to be valid, so it might not be included in the bank.
# If multiple mutations are needed, all mutations during in the sequence must be valid.
# You may assume start and end string is not the same.


# Example 1:
#
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
#
# return: 1
#
# Example 2:
#
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#
# return: 2
#
#
# Example 3:
#
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
#
# return: 3


from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        from collections import defaultdict, deque

        dq = deque()
        mp = defaultdict(set)
        gp = defaultdict(set)
        bank = set(bank)

        if end not in bank:
            return -1

        bank.add(start)

        for i in bank:
            for j in range(len(i)):
                mp[i[:j] + "*" + i[j + 1:]].add(i)

        for i in bank:
            for j in range(len(i)):
                gene = i[:j] + "*" + i[j + 1:]
                gp[i].update(mp[gene])
            gp[i].discard(i)

        dq.append(start)
        visited = set()
        visited.add(start)
        count = 0
        while dq:
            for _ in range(len(dq)):
                curr = dq.popleft()
                for i in gp[curr]:
                    if i == end:
                        return count + 1
                    if i not in visited:
                        visited.add(i)
                        dq.append(i)
            count += 1

        return -1


if __name__ == "__main__":
    print(Solution().minMutation("AAAACCCC", "CCCCCCCC", ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]))
