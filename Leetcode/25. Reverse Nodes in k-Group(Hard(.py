# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count, node = 0, head

        while node:
            count += 1
            node = node.next

        if k <= 1 or count < k:
            return head
        pre, cur = None, head
        for _ in range(k):
            cur.next, pre, cur = pre, cur, cur.next

        head.next = self.reverseKGroup(cur, k)

        return pre


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a1.next = a2
a2.next = a3
a3.next = a4

print(Solution().reverseKGroup(a1, 2))
