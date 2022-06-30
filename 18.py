# 클래스 생성
class Car:

    def __init__(self, col, len):
        self.color = col
        self.length = len

    def doStop(self):
        print('STOP!')

    def doStart(self):
        print('START!')

    def printinfo(self):
        print(f'color : {self.color}')
        print(f'length : {self.length}')

# 객체 생성 by,생성자 호출
# Car()를 '생성자 호출' 이라 하고, 그 안에 변수를 넣어 color과 length를 선언하는 것을 '속성값 초기화'라고 한다다
Car1 = Car('red',200)
Car2 = Car('blue', 300)

Car1.printinfo()
Car2.printinfo()