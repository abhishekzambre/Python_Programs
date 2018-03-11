class Test:
    def __init__(self):
        self.subset = []
        self.n = 3

    def search(self, k):
        if k == self.n:
            print(self.subset)
            return
        else:
            self.search(k+1)
            self.subset.append(k)
            self.search(k+1)
            self.subset.pop()


obj = Test()
obj.search(0)
