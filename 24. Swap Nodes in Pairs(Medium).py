# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return

        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first
            cur = cur.next.next

        return dummy.next


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a1.next = a2
a2.next = a3
a3.next = a4
print(a1)
print(Solution().swapPairs(a1))
