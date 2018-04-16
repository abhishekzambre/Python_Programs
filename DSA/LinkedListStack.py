class LinkedListStack:
    """
    LinkedListStack Abstract Data Type

    L.push(value)
    L.pop()

    L.top()
    L.isEmpty()
    len(L)
    L.print()
    """

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
        self._size = 0
        pass

    def isEmpty(self):
        return self._head is None

    def __len__(self):
        return self._size

    def top(self):
        if self.isEmpty():
            raise ValueError("Stack is empty")
        return self._head.getValue()

    def push(self, value):
        self._head = self._Node(value, self._head)
        self._size += 1
        print(value, "pushed to stack successfully.")

    def pop(self):
        if self.isEmpty():
            raise ValueError("Stack is empty")
        target = self._head.getValue()
        self._head = self._head.getNext()
        self._size -= 1
        return target

    def print(self):
        temp = self._head
        print("head", end="\t->\t")
        while temp:
            print(temp.getValue(), end="\t->\t")
            temp = temp.getNext()
        print("None")


ll = LinkedListStack()
print("Stack empty?:", ll.isEmpty())
print("Stack size:", len(ll))
ll.push(4)
ll.push(7)
ll.push(2)
ll.push(9)
print("Stack empty?:", ll.isEmpty())
print("Stack size:", len(ll))
ll.print()
print("Top of the stack:", ll.top())
x = ll.pop()
print(x, "popped successfully.")
ll.print()
print("Stack size:", len(ll))
x = ll.pop()
print(x, "popped successfully.")
x = ll.pop()
print(x, "popped successfully.")
x = ll.pop()
print(x, "popped successfully.")
ll.print()
# x = ll.pop()
