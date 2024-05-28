# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        temp = head
        count = 1
        while temp.next:
            temp = temp.next
            count += 1

        k %= count
        if not k or count <= 1:
            return head

        slow = fast = head

        for _ in range(k):
            fast = fast.next
        ### we will keep the first point  i mean the one we want to rotate first point
        while fast.next:
            slow = slow.next
            fast = fast.next

        newhead = fast
        slow.next = None
        fast.next = head
        head = newhead
        return head


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a1.next = a2
a2.next = a3
a3.next = a4

print(Solution().rotateRight(a1, 1))
