# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        l = self.sortList(head)
        r = self.sortList(mid)

        def merge2list(left, right):
            if not left or not right:
                return left or right

            cur = dummy = ListNode(0)
            while left and right:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next

            cur.next = left or right
            return dummy.next

        return merge2list(l, r)


a1 = ListNode(1)
a11 = ListNode(2)
a2 = ListNode(3)
a3 = ListNode(4)
# a4 = ListNode(5)
a1.next = a11
a11.next = a2
a2.next = a3
# a3.next = a4


print(Solution().sortList(a1))
