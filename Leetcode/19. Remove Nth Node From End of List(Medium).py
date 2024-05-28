# Definition for singly-linked list.
# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head

        slow = fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next
