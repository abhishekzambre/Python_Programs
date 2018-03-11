class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, key, value):
        self._coords[key] = value

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')

        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] + other[j]

        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "<" + str(self._coords)[1:-1] + ">"


o1 = Vector(10)
o1[2] = 4
o2 = Vector(11)

print(str(o1))

print(o1[2])
print(len(o1))
print(o2)
print(o1 == o2)


for i in o1:
    print(i)
