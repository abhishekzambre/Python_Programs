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


class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.value

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node.next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header.next)

    def last(self):
        return self._make_position(self._trailer.prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node.prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, pred, val, succ):
        node = super()._insert_between(pred, val, succ)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(self._header, e, self._header.next)

    def add_last(self, e):
        return self._insert_between(self._trailer.prev, e, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(original.prev, e, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(original, e, original.next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old = original.value
        original.value = e
        return old


pl = PositionalList()
p = pl.add_first(10)
print(p.element())
p2 = pl.add_after(p, 20)
print(p2.element())
p3 = pl.add_last(40)

cursor = pl.first()
while cursor is not None:
    print(cursor.element(), end="a")
    cursor = pl.after(cursor)