class Fancy:
    def __init__(self):
        self.sequence = []
        self.length = 0


    def append(self, val: int) -> None:
        self.sequence.append(val)
        self.length += 1


    def addAll(self, inc: int) -> None:
        self.sequence = [i  + inc for i in self.sequence]


    def multAll(self, m: int) -> None:
        self.sequence = [i * m for i in self.sequence]


    def getIndex(self, idx: int) -> int:
        if idx >= self.length:
            return -1
        else:
            return self.sequence[idx] % 1000000007



# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)