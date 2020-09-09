import queue
class MaxQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.dequeue = queue.deque()

    def max_value(self) -> int:
        return self.dequeue[0] if self.dequeue else -1

    def push_back(self, value: int) -> None:
        while self.dequeue and self.dequeue[-1] < value:
            self.dequeue.pop()
        self.dequeue.append(value)
        self.queue.put(value)


    def pop_front(self) -> int:
        if self.queue.qsize() == 0:
            return -1
        q = self.queue.get()
        if q == self.dequeue[0]:
            self.dequeue.popleft()
        return q


obj = MaxQueue()
print(obj.pop_front())
print(obj.pop_front())
print(obj.pop_front())
print(obj.pop_front())
print(obj.pop_front())
obj.push_back(15)
print(obj.max_value())
obj.push_back(9)
print(obj.max_value())