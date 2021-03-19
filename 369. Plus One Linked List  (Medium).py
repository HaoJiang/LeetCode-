# Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.
#
# Example:
#
# Input:
# 1->2->3
#
# Output:
# 1->2->4

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def plus1number(self, head):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        pre = dummy = ListNode(0)

        dummy.next = head

        def dfs(dummy, number):
            if not dummy:
                return 1
            next = dfs(dummy.next, number)
            nval, val = divmod(next + dummy.val, 10)
            dummy.val = val
            return nval

        dfs(dummy, 0)

        return 1 if pre else 2


a1 = ListNode(9)
a11 = ListNode(9)
a2 = ListNode(9)
a3 = ListNode(9)
a4 = ListNode(9)
a1.next = a11
a11.next = a2
a2.next = a3
a3.next = a4

print(Solution().plus1number(a1))
