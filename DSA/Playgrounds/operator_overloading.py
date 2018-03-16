class Test:
	def __init__(self, data):
		self._data=data

	def get_data(self):
		return self._data

	def __add__(self, Test):
		return self._data + Test.get_data()


A = Test(10)
B = Test(20)

print("A : ", A.get_data())
print("B : ", B.get_data())

print("A+B : ", A+B)

C = Test(A+B)

print("C : ", C.get_data())