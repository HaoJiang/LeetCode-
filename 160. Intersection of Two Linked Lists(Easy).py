# Write a program to find the node at which the intersection of two singly linked lists begins.
#
# For example, the following two linked lists:

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def getIntersectionNode_sec(self, headA, headB):

        # a + c + b = b + c + a

        ### loop the end will be same node or none

        curA = headA
        curB = headB

        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        def getdepth(head):
            count = 0
            while head:
                head = head.next
                count += 1
            return count

        curA = headA
        curB = headB
        countA = getdepth(curA)
        countB = getdepth(curB)

        if countA > countB:
            dif = countA - countB
            while dif:
                headA = headA.next
                dif -= 1
        if countB > countA:
            dif = countA - countB
            while dif:
                headB = headB.next
                dif -= 1

        while headA:
            if headA.val == headB.val:
                return headA.val
            headA = headA.next
            headB = headB.next
        return None
