class CircularQueue:
    """
    CircularQueue Abstract Data Type

    L.enqueue(value)
    L.dequeue()

    L.first()
    L.isEmpty()
    len(L)
    L.print()
    """
    __slots__ = '_tail', '_size'

    class _Node:
        __slots__ = '_value', '_next'

        def __init__(self, value, next):
            self._value = value
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def first(self):
        if self.isEmpty():
            raise ValueError("Queue is empty")
        head = self._tail._next
        return head._value

    def enqueue(self, value):
        new = self._Node(value, None)
        if self.isEmpty():
            new._next = new
        else:
            new._next = self._tail._next
            self._tail._next = new
        self._tail = new
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise ValueError("Queue is empty")
        target = self._tail._next

        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = target._next

        self._size -= 1
        return target._value

    def print(self):
        temp = self._tail._next
        print("First", end="\t->\t")
        for i in range(self._size):
            print(temp._value, end="\t->\t")
            temp = temp._next
        print("None")


cq = CircularQueue()
print("Is Queue empty?:", cq.isEmpty())
print("Queue size:", len(cq))
cq.enqueue(10)
cq.enqueue(30)
cq.enqueue(40)

print("Is Queue empty?:", cq.isEmpty())
print("Queue size:", len(cq))

cq.print()

print(cq.dequeue())
