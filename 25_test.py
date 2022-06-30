class BasicCal:
    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2


class DevelopCal:
    def mod(self, n1, n2):
        return n1 % n2

    def flo(self, n1, n2):
        return n1 // n2

    def exp(self, n1, n2):
        return n1 ** n2

class NewCal(BasicCal, DevelopCal):
    def __init__(self):
        pass


my = NewCal()

print(f'my.add(10, 20) : {my.add(10, 20)}')
print(f'my.sub(10, 20) : {my.sub(10, 20)}')
print(f'my.mul(10, 20) : {my.mul(10, 20)}')
print(f'my.div(10, 20) : {my.div(10, 20)}')
print(f'my.mod(10, 20) : {my.mod(10, 20)}')
print(f'my.flo(10, 20) : {my.flo(10, 20)}')
print(f'my.exp(2, 5) : {my.exp(2, 5)}')