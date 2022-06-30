# 계산기 추상 클래스를 만들고 이를 이용해서 새로운 계산기 클래스를 만들어보자
# 추상 클래스에는 덧, 뺄, 곱, 나눗 기능이 있어야 한다.
from abc import ABCMeta
from abc import abstractmethod
class Cal(metaclass=ABCMeta):

    @abstractclassmethod
    def add(self, n1, n2):
        pass

    @abstractclassmethod
    def sub(self, n1, n2):
        pass

    @abstractclassmethod
    def mul(self, n1, n2):
        pass

    @abstractclassmethod
    def div(self, n1, n2):
        pass


class MyCal(Cal):
    def add(self, n1, n2):
        print(n1 + n2)

    def sub(self, n1, n2):
        print(n1 - n2)

    def mul(self, n1, n2):
        print(n1 * n2)

    def div(self, n1, n2):
        print(n1 / n2)

    def exp(self, n1, n2):
        print(n1 ** n2)

    def flo(self, n1, n2):
        print(n1 // n2)

    def mod(self, n1, n2):
        print(n1 % n2)