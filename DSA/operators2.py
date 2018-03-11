class Range:

    def __init__(self, start, stop = None, step = 1):
        if step == 0:
            raise ValueError('Step cannot be 0')

        if stop is None:
            start, stop = 0, start

        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('Index out of range')

        return self._start + k * self._step


obj = Range(10, 0, -1)
for i in obj:
    print(i)

class A:
    def __init__(self, a):
        self._a = a

class B:
    def __init__(self, b):
        self._b = b


class C(A, B):
    def __init__(self, a, c):
        super().__init__(a)
        self._c = c


obj1 = C(5, 10)
print(obj1._c, obj1._a)