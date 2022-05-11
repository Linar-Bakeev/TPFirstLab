class Summator:
    def transform(self, n):
        return n

    def sum(self, n):
        res = 0
        for i in range(1, n + 1):
            res += self.transform(i)
        return res


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3


print(Summator().sum(5))
print(SquareSummator().sum(5))
print(CubeSummator().sum(5))
