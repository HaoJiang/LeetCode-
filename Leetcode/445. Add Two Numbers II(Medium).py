# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1stack, l2stack = [], []

        while l1:
            l1stack.append(l1.val)
            l1 = l1.next

        while l2:
            l2stack.append(l2.val)
            l2 = l2.next

        carry = 0

        pre = None
        while l1stack or l2stack or carry:
            a = l1stack.pop() if l1stack else 0
            b = l2stack.pop() if l2stack else 0
            carry, k = divmod((a + b + carry), 10)
            node = ListNode(k)
            node.next = pre
            pre = node

        return pre
