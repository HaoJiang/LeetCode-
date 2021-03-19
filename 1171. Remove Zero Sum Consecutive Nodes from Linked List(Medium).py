# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:

        from collections import defaultdict

        cache = defaultdict(ListNode)

        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        prefixsum = 0
        while p:
            prefixsum += p.val
            cache[prefixsum] = p
            p = p.next

        prefixsum = 0
        p = dummy
        while p:
            prefixsum += p.val
            p.next = cache[prefixsum].next
            p = p.next
        return dummy.next




