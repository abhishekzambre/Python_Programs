class ArrayQueue:

    def __init__(self, capacity):
        self._data = [None] * capacity
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def first(self):
        if self.isEmpty():
            raise ValueError("Queue is empty")
        return self._data[self._front]

    def enqueue(self, value):
        if self._size == len(self._data):
            self.resize(2 * len(self._data))

        position = (self._front + self._size) % len(self._data)
        self._data[position] = value
        self._size += 1

    def resize(self, capacity):
        old = self._data
        self._data = [None] * capacity
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def deque(self):
        if self.isEmpty():
            raise ValueError("Queue is empty")
        target = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return target

    def print(self):
        print(self._data)


q = ArrayQueue(5)
q.print()
print(q.isEmpty())

q.enqueue(10)
q.print()

q.enqueue(20)
q.print()

print(q.deque())

q.print()

q.enqueue(30)
q.enqueue(40)
q.print()
q.deque()
q.enqueue(50)
q.print()
q.enqueue(60)
q.print()
q.enqueue(70)
q.print()
q.enqueue(10)
q.print()
print(q.deque())
q.print()
q.enqueue(20)
q.print()
print(len(q))
print(q.isEmpty())