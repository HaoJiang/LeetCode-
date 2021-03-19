# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example 1:
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Splits in place a list in two halves, the first half is >= in size than the second.
    # @return A tuple containing the heads of the two halves

class Solution:

    # @param head, a ListNode
    # @return nothing
    # def reorderList(self, head):
    #     if not head or not head.next:
    #         return
    #
    #     def _splitList(head):
    #         fast = head
    #         slow = head
    #         while fast and fast.next:
    #             slow = slow.next
    #             fast = fast.next.next
    #
    #         middle = slow.next
    #         slow.next = None
    #
    #         return head, middle
    #
    #     # Reverses in place a list.
    #     # @return Returns the head of the new reversed list
    #     def _reverseList(head):
    #
    #         last = None
    #         currentNode = head
    #
    #         while currentNode:
    #             nextNode = currentNode.next
    #             currentNode.next = last
    #             last = currentNode
    #             currentNode = nextNode
    #
    #         return last

        # Merges in place two lists
        # @return The newly merged list.
        # def _mergeLists(a, b):
        #
        #     tail = a
        #     head = a
        #
        #     a = a.next
        #     while b:
        #         tail.next = b
        #         tail = tail.next
        #         b = b.next
        #         if a:
        #             a, b = b, a
        #
        #     return head
        #
        # a, b = _splitList(head)
        # b = _reverseList(b)
        # head = _mergeLists(a, b)
        #
        # return head


    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        def splitlt(_head):
            slow = fast = _head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            k = slow.next
            slow.next = None
            return _head, k

        def reverselk(_head):
            pre = None
            while _head:
                _head.next, pre, _head = pre, _head, _head.next

            return pre

        m, n = splitlt(head)

        n = reverselk(n)

        while n:
            next1, next2 = m.next, n.next
            m.next = n
            n.next = next1
            m, n = next1, next2

        print(m)


a1 = ListNode(1)
a11 = ListNode(2)
a2 = ListNode(3)
a3 = ListNode(4)
a4 = ListNode(5)
a1.next = a11
a11.next = a2
a2.next = a3
a3.next = a4

print(Solution().reorderList(a1))
