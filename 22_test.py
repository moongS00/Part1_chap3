# 덧셈, 뺄셈기능이 있는 클래스를 만들고, 이를 상속하는 클래스를 만들어서 곱셈과 나눗셈 기능을 추가해보자
class Cal1:

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2


class Cal2(Cal1):

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2


a = Cal2()
print(a.add(10, 20))
print(a.sub(10, 20))
print(a.mul(10, 20))
print(a.div(10, 20))



