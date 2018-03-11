class Solution(object):

    def __init__(self):
        self.par_set = []
        self.all_perm = []
        self.chosen = []
        self.n = 0
        self.out = []
        self.par_stack = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        self.n = n * 2

        for i in range(n):
            self.par_set.append("(")
            self.par_set.append(")")

        self.chosen = [0] * self.n

        self.generate()

        return sorted(set(self.out))


    def generate(self):

        if len(self.all_perm) == self.n:
            # print(self.all_perm)
            if self.check_valid(self.all_perm):
                self.out.append(''.join(self.all_perm))
        else:
            for i in range(self.n):
                if self.chosen[i]:
                    continue

                self.chosen[i] = True
                self.all_perm.append(self.par_set[i])
                self.generate()
                self.chosen[i] = False
                self.all_perm.pop()

        pass

    def check_valid(self, cur_set):
        for c in cur_set:
            if c == "(":
                self.par_stack.append(c)
            else:
                if len(self.par_stack) == 0:
                    return False
                self.par_stack.pop()

        if len(self.par_stack) == 0:
            return True
        else:
            return False


obj = Solution()
print(obj.generateParenthesis(5))
