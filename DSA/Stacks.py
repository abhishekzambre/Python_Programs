class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = [] # nonpublic list instance

    def len (self):
        """Return the number of elements in the stack."""
        return len(self. _data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e) # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty( ):
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))  # we will re-insert newlines when writing
    original.close()

    # now we overwrite with contents in LIFO order
    output = open(filename, 'w')  # reopening file overwrites original
    while not S.is_empty():
        output.write(S.pop() + '\n')  # re-insert newline characters
    output.close()


reverse_file('test.txt')
