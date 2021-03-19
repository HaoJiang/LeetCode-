# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        def reverselinklist(nhead):

            pre = None

            while nhead:
                nhead.next, pre, nhead = pre, nhead, nhead.next

            return pre

        if not head or not head.next:
            return True

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #  because 1 -- 2 -- 2 --2 -- 1  pre = 1 --  2 -- 2  no need to right this line
        # if fast:
        #     slow = slow.next

        cur = reverselinklist(slow)

        while cur:
            if cur.val != head.val:
                return False
            cur = cur.next
            head = head.next

        return True
