# 계산기 클래스 만들기(클래스에 매개변수가 없는 경우)
class Cal:

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.res = 0

    def add(self):
        self.res = self.num1 + self.num2
        return self.res

    def sub(self):
        self.res = self.num1 - self.num2
        return self.res

    def mul(self):
        self.res = self.num1 * self.num2
        return self.res

    def div(self):
        self.res = self.num1 / self.num2
        return self.res


a = Cal()      # 클래스 호출(매개변수가 없으니 ()는 빈칸)
a.num1 = 10    # 각각 초기화 해주기
a.num2 = 20
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

