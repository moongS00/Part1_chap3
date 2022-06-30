# 객체와 메모리
class Robot:

    def __init__(self, c, h, w):
        self.color = c
        self.height = h
        self.weight = w

    def info(self):
        print(f'color : {self.color}')
        print(f'height : {self.height}')
        print(f'weight : {self.weight}')


# 우리는 객체에 접근할 수 없어서
# 변수를 만든다. & 변수에 객체의 메모리 주소를 할당 한다.
# 변수 = 객체
rb1 = Robot('red', 200, 80)
rb2 = Robot('blue', 300, 120)
rb3 = rb1  # rb3에는 rb1이 갖고 있는 메모리 주소가 복사됨

rb1.info()
rb2.info()
rb3.info()

rb1.color = 'gray'
rb1.height = 100
rb1.weight = 50

rb1.info()
rb2.info()
rb3.info()  # rb1의 속성만 바꿨지만 rb3의 속성도 같이 바뀜 (메모리 주소의 값이 복사된 것이기 때문)
