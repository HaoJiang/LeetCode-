# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq

        sec = []
        cur = dummy = ListNode(0)

        for i in lists:
            if i:
                heapq.heappush(sec, (i.val, i))

        while sec:
            node, lk = heapq.heappop(sec)
            cur.next = ListNode(node)
            cur = cur.next
            if lk.next:
                heapq.heappush(sec, (lk.next.val, lk.next))

        cur.next = None

        return dummy.next

