# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# Example:
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # two list assist

        cur1 = dummy1 = ListNode(0)
        cur2 = dummy2 = ListNode(0)

        while head:
            if head.val < x:
                cur1.next = head
                cur1 = cur1.next
            else:
                cur2.next = head
                cur2 = cur2.next
            head = head.next

        cur2.next = None
        cur1.next = dummy2.next
        return dummy1.next


a1 = ListNode(4)
a11 = ListNode(1)
a2 = ListNode(1)
a3 = ListNode(2)
a4 = ListNode(6)
a1.next = a11
a11.next = a2
a2.next = a3
a3.next = a4

print(Solution().partition(a1, 2))
