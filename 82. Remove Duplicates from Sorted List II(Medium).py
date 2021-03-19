# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# Return the linked list sorted as well.
#
# Example 1:
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# Example 2:
#
# Input: 1->1->1->2->3
# Output: 2->3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return

        pre = dummy = ListNode(0)
        dummy.next = head

        cur = head

        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next

                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next

        return dummy.next


a1 = ListNode(1)
a11 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a1.next = a11
a11.next = a2
a2.next = a3
a3.next = a4

print(Solution().deleteDuplicates(a1))
