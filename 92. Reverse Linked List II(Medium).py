# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        p = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            p = p.next
        cur = p.next
        pre = None
        for _ in range(n - m + 1):
            # temp = cur.next
            # cur.next = pre
            # pre = cur
            # cur = temp
            cur.next, pre, cur = pre, cur, cur.next
        p.next.next = cur
        p.next = pre
        return dummy.next

        # def reverselk(head1, count):
        #     pre = None
        #     while head1 and count:
        #         # temp = head.next
        #         # head.next = pre
        #         # pre = head
        #         # head = temp
        #
        #         head1.next, pre, head1 = pre, head1, head1.next
        #         count -= 1
        #
        #     tmp = pre
        #
        #     while tmp.next:
        #         tmp = tmp.next
        #     if head1:
        #         tmp.next = head1
        #
        #     return pre
        #
        # k = n - m
        # if not k:
        #     return head
        #
        # cur = dummy = ListNode(0)
        #
        # dummy.next = head
        #
        # m -= 1
        #
        # while cur and m:
        #     cur = cur.next
        #     m -= 1
        #
        # cur.next = reverselk(cur.next, k + 1)

        # return dummy.next


a1 = ListNode(1)
a11 = ListNode(2)
a2 = ListNode(3)
a3 = ListNode(4)
a4 = ListNode(5)
a1.next = a11
a11.next = a2
a2.next = a3
a3.next = a4

print(Solution().reverseBetween(a1, 2, 4))
