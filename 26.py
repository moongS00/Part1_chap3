'''
오버라이딩
하위 클래스에서 상위 클래스의 매서드를 재정의(override)한다
'''
class Robot:
    def __init__(self, c, h, w):
        self.color = c
        self.height = h
        self.weight = w

    def fire(self):
        print('총알 발사!')

    def info(self):
        print(f'color : {self.color}')
        print(f'height : {self.height}')
        print(f'weight : {self.weight}')

class NewRobot(Robot):
    def __init__(self, c, h, w):
        super().__init__(c, h, w)

    def fire(self):
        print('레이저 발사!')

m = NewRobot('red', 100, 900)
m.info()
m.fire()   #상위 클래스로 올라가지 않음!
