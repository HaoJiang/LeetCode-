# class Node:
#     def __init__(self, val=None):
#         self.perv = None
#         self.next = None
#         self.val = val
#
#
# class DoubleLinklist:
#     def __init__(self):
#         self.head = Node()
#         self.tail = Node()
#         self.head.next = self.tail
#         self.tail.perv = self.head


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        # self.doubleLK = DoubleLinklist()
        self.arr = []
        self.size = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map:
            return False
        self.arr.append(val)
        self.size += 1
        self.map[val] = self.size - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map:
            return False

        idx = self.map[val]
        if idx != self.size - 1:
            curr = self.arr[-1]
            self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
            self.map[curr] = idx
        self.map.pop(val)
        self.arr.pop()
        self.size -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        if not self.size:
            return None
        print(self.arr[random.randint(0, self.size - 1)])
        return self.arr[random.randint(0, self.size - 1)]


obj = RandomizedSet()
param_1 = obj.insert(0)
param_1 = obj.remove(0)
param_1 = obj.insert(-1)
param_1 = obj.remove(0)
param_3 = obj.getRandom()
param_3 = obj.getRandom()
param_3 = obj.getRandom()
param_3 = obj.getRandom()
param_3 = obj.getRandom()