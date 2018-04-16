class _DoublyLinkedBase:
    class _Node:
        __slots__ = 'prev', 'value', 'next'

        def __init__(self, prev, value, next):
            self.prev = prev
            self.value = value
            self.next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, pred, val, succ):
        new = self._Node(pred, val, succ)
        self._header.next = new
        self._trailer.prev = new
        self._size += 1
        return new

    def _delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self._size -= 1
        val = node.value
        node.prev = node.value = node.next = None
        return val


class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise ValueError("Deque is empty")
        return header.next.value

    def last(self):
        if self.is_empty():
            raise ValueError("Deque is empty")
        return trailer.prev.value

    def insert_first(self, value):
        self._insert_between(self._header, value, self._header.next)

    def insert_last(self, value):
        self._insert_between(self._trailer.prev, value, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self._delete_node(self._header.next)

    def delete_last(self):
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self._delete_node(self._trailer.prev)
