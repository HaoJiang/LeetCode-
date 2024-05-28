class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        ## O(n)   Space O(1)

        if not head:
            return head

        first = second = curr = head

        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next

        while first:
            if first.random:
                first.next.random = first.random.next
            first = first.next

        dummy = Node()

        while second:
            dummy.next = second.next
            second = second.next.next
        return dummy.next




        ##  O(n)  Space( O(n))
        # if not head:
        #     return []
        #
        # map = {}
        # curr = head
        # while curr:
        #     new_node = Node(curr.val)
        #     map[curr] = new_node
        #     curr = curr.next
        #
        # curr = head
        #
        # while curr:
        #     if curr.next:
        #         map[curr].next = map[curr.next]
        #     if curr.random:
        #         map[curr].random = map[curr.random]
        #     curr = curr.next
        # return map[head]
