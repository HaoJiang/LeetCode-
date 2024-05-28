from collections import defaultdict


class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.freq = 0
        self.next = None
        self.prev = None


class Doublelinklist:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def pop(self, node=None):
        if not node:
            node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minfreq = 1
        self.cache = {}
        self.freqmap = defaultdict(Doublelinklist)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.increasefreq(node)
        return node.val

    def increasefreq(self, node):
        if node.freq:
            self.freqmap[node.freq].pop(node)
            self.ckfreqmap(node.freq)
        node.freq += 1
        self.freqmap[node.freq].append(node)
        self.minfreq = min(self.minfreq, node.freq)

    def ckfreqmap(self, freq):
        if not self.freqmap[freq].size:
            if freq == self.minfreq:
                self.minfreq = freq + 1

    def put(self, key: int, value: int) -> None:
        if self.capacity > 0:
            if key in self.cache:
                node = self.cache[key]
                node.val = value
            else:
                node = Node(key, value)
                self.cache[key] = node
                self.size += 1
            if self.size > self.capacity:
                delelekey = self.freqmap[self.minfreq].pop()
                del self.cache[delelekey.key]
                if not self.freqmap[self.minfreq].size:
                    self.minfreq = 1
                self.size -= 1
            self.increasefreq(node)


# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(3)
obj.put(2, 2)
obj.put(1, 1)
obj.get(2)
obj.get(1)
obj.get(2)
obj.put(3, 3)
obj.put(4, 4)
obj.get(3)
obj.get(2)
obj.get(1)
obj.get(4)
