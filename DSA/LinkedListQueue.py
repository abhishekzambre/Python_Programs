class LinkedListQueue:
    """
    LinkedListQueue Abstract Data Type

    L.enqueue(value)
    L.dequeue()

    L.first()
    L.isEmpty()
    len(L)
    L.print()
    """
    __slots__ = '_head', '_tail', '_size'

    class _Node:
        __slots__ = '_value', '_next'

        def __init__(self, value, next):
            self._value = value
            self._next = next

        def setValu(self, value):
            self._value = value

        def getValue(self):
            return self._value

        def setNext(self, next):
            self._next = next

        def getNext(self):
            return self._next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self):
        return self._head is None

    def __len__(self):
        return self._size

    def first(self):
        if self.isEmpty():
            raise ValueError("Queue is empty")
        return self._head.getValue()

    def enqueue(self, value):
        temp = self._Node(value, None)

        if self.isEmpty():
            self._head = temp
        else:
            self._tail._next = temp
        self._tail = temp
        self._size += 1
        print(value, "pushed to queue successfully.")

    def dequeue(self):
        if self.isEmpty():
            raise ValueError("Queue is empty")
        target = self._head.getValue()
        self._head = self._head.getNext()
        self._size -= 1
        if self.isEmpty():
            self._tail = None
        return target

    def print(self):
        temp = self._head
        print("head", end="\t->\t")
        while temp:
            print(temp.getValue(), end="\t->\t")
            temp = temp.getNext()
        print("None")
        temp = self._head
        print("\t", end="\t")
        while temp:
            if temp == self._tail:
                print("tail^", end="\t")
            else:
                print("\t", end="\t")
            temp = temp.getNext()
        print()


ll = LinkedListQueue()
print("Queue empty?:", ll.isEmpty())
print("Queue size:", len(ll))
ll.enqueue(4)
ll.enqueue(7)
ll.enqueue(2)
ll.enqueue(9)
print("Stack empty?:", ll.isEmpty())
print("Stack size:", len(ll))
ll.print()
print("Top of the queue:", ll.first())
x = ll.dequeue()
print(x, "dequeued successfully.")
ll.print()
print("Stack size:", len(ll))
x = ll.dequeue()
print(x, "dequeued successfully.")
x = ll.dequeue()
print(x, "dequeued successfully.")
x = ll.dequeue()
print(x, "dequeued successfully.")
ll.print()
print(ll._tail)
ll.enqueue(10)
ll.enqueue(20)
ll.print()
# x = ll.dequeue()
