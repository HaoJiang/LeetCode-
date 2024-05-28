class FreqStack:

    def __init__(self):
        from collections import defaultdict
        self.freq = defaultdict(int)
        self.group_map = defaultdict(list)
        self.max_freq = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        if self.max_freq < self.freq[x]:
            self.max_freq = self.freq[x]
        self.group_map[self.freq[x]].append(x)

    def pop(self) -> int:
        if self.max_freq:
            curr = self.group_map[self.max_freq].pop()
            self.freq[curr] -= 1
            if not self.group_map[self.max_freq]:
                self.max_freq -= 1
        return curr

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
