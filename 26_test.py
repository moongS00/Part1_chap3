# 삼각형 넓이를 계산하는 클래스를 만들고 이를 상속하는 클래스에서
# getArea()를 오버라이딩 해서 출력 결과가 다음과 같을 수 있도록 클래스를 만들어보자
class TriArea:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def info(self):
        print(f'width : {self.width}')
        print(f'height : {self.height}')

    def getArea(self):
        return self.width * self.height /2

class NewTri(TriArea):
    def __init__(self, w, h):
        super().__init__(w, h)

    def getArea(self):
        return str(super().getArea()) + '㎠'

my = NewTri(7, 5)
my.info()
print(f'my.getArea() : {my.getArea()}')