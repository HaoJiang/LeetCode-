# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
# Example 1:
#
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# Example 2:
#
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return

        odd = head
        evenhead = even = head.next

        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd, even = odd.next, even.next

        odd.next = evenhead

        return head


a1 = ListNode(1)
a11 = ListNode(2)
a2 = ListNode(3)
a3 = ListNode(4)
a4 = ListNode(5)
# a5 = ListNode(6)
a1.next = a11
a11.next = a2
a2.next = a3
a3.next = a4
# a4.next = a5

print(Solution().oddEvenList(a1))
