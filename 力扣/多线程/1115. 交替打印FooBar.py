import threading
import queue
class FooBar:
    def __init__(self, n):
        self.n = n
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.q1.put(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.q1.get()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.q2.put(0)


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.q2.get()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.q1.put(0)

def printFoo():
    print('Foo', end='')

def printBar():
    print('Bar', end='')

fb = FooBar(5)
t1 = threading.Thread(target=fb.foo, args=(printFoo, ))
t2 = threading.Thread(target=fb.bar, args=(printBar, ))
t1.start()
t2.start()