from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []

        def _countlk(node: ListNode) -> int:
            count = 0
            while node:
                count += 1
                node = node.next
            return count

        cnt = _countlk(head)

        if not cnt:
            return [ListNode() for _ in range(k)]
        elif cnt <= k:
            while head:
                res.append(ListNode(head.val))
                head = head.next
            res += [ListNode() for _ in range(k - cnt)]
        else:
            t, left = divmod(cnt, k)

            for sl in range(t):
                tp = []
                for _ in range(k):
                    curr = head
                    tp.append(curr)
                    head = curr.next
                    curr.next = None
                if left:
                    curr = head
                    tp.append(curr)
                    head = curr.next
                    curr.next = None
                    left -= 1
                res.append(tp)

        return res


if __name__ == "__main__":
    print(Solution().splitListToParts())

