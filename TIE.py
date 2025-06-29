class TIE:
    def __init__(self, x):
        self.n = len(x)
        self.memo = [[-1 for i in range(self.n)] for j in range(self.n)]
        self.sum = 0
        self.comp = 0
        for j in range(self.n):
            self.memo[0][j] = x[j]  # base cases
        for i in range(self.n):
            self.memo[i][self.n - 1] = x[self.n - 1 - i]  # base cases
        self.value = self.rec_tie(self.n - 1, 0)

    def rec_tie(self, i: int, j: int) -> float:
        if self.memo[i][j] == -1:  # unsolved cases
            self.memo[i][j] = max(self.rec_tie(i - 1, j), self.rec_tie(i - 1, j) + self.rec_tie(i, j + 1))
            self.sum += 1
            self.comp += 1

        return self.memo[i][j]


def tie(x):
    k = TIE(x)
    return k.value


def t(x):
    k = TIE(x)
    return k.sum, k.comp  # we would expect this to be (n - 1)^2 in both cases.
