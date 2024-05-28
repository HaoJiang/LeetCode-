class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.map = defaultdict(set)
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.map[val].add(len(self.arr))
        self.arr.append(val)
        if len(self.map[val]) > 1:
            return False
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.map:
            return False
        idx = self.map[val].pop()
        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.map[self.arr[idx]].add(idx)
        self.map[self.arr[idx]].discard(len(self.arr) - 1)
        if not self.map[val]:
            del self.map[val]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        import random

        return random.choice(self.arr)

# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
param_1 = obj.insert(0)
param_1 = obj.remove(0)
param_1 = obj.insert(-1)
param_1 = obj.remove(0)
param_3 = obj.getRandom()
