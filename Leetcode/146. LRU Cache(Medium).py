class doublelinklsit:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head = doublelinklsit()
        self.tail = doublelinklsit()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        curr_node = self.cache[key]
        self.movetohead(curr_node)
        return curr_node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = doublelinklsit(key, value)
            self.cache[key] = node
            self.insert(node)
            self.size += 1
            if self.size > self.capacity:
                deletekey = self.removelastone()
                del self.cache[deletekey]
                self.size -= 1
            return
        curr_node = self.cache[key]
        if curr_node.val != value:
            curr_node.val = value
        self.movetohead(curr_node)
        return

    def movetohead(self, node):
        if node.prev == self.head:
            return
        self.remove(node)
        self.insert(node)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def removelastone(self):
        node = self.tail.prev
        self.remove(node)
        return node.key


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)

obj.put(1, 0)
obj.put(2, 2)
param_1 = obj.get(1)
obj.put(3, 3)
param_1 = obj.get(2)
obj.put(4, 4)
param_1 = obj.get(1)
param_1 = obj.get(3)
param_1 = obj.get(4)
