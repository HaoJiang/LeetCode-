# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:

        fast, slow, curr = head, head, head

        i = 1
        while curr:
            if i < k:
                slow = slow.next

            if i > k:
                fast = fast.next

            curr = curr.next
            i += 1

        slow.val, fast.val = fast.val, slow.val

        return head

