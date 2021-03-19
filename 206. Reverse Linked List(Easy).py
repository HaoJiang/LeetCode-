# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return
        cur = head
        pre = None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        # while cur:
        #     temp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = temp
        return pre
