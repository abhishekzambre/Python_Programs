import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("Index out of bound")

        return self._A[k]

    def append(self, item):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = item
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]

        self._A = B
        self._capacity = c

    def getCapacity(self):
        return self._capacity

    def insert(self, k, value):
        if self._n == self._capacity:
            _resize(2 * self._capacity)

        for i in range(self._n, k, -1):
            self._A[i] = self._A[i-1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):

        for i in range(self._n):
            if self._A[i] == value:
                for j in range(i, self._n-1):
                    print("in remove", i, j, self._n)
                    self._A[j] = self._A[j+1]
                self._A[self._n-1] = None
                self._n -= 1
                return


dyn_arr = DynamicArray()
print(dyn_arr.getCapacity())
print(len(dyn_arr))

dyn_arr.append(2)
dyn_arr.append(5)

print(len(dyn_arr))

dyn_arr.append(7)

dyn_arr.insert(2, 13)

print(dyn_arr.getCapacity())

for i in dyn_arr:
    print(i, end=" ")

print()
dyn_arr.remove(5)
print()
for i in dyn_arr:
    print(i, end=" ")
