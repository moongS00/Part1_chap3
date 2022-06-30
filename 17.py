'''
#17. 객체지향 프로그래밍

객체(object) = 속성(attribute) + 기능(function)
객체는 클래스(class)에서 생성된다

클래스를 미리 만들어두면 객체를 반복해서 만들어낼 수 있다

객체: 코드 재사용, 모듈화에 좋다
'''


# 18.클래스와 객체 생성
# 클래스 선언(첫글자는 대문자)
class Car:

    def __int__(self, col, len):  # 생성자, 속성
        self.color = col  # 속성1
        self.length = len  # 속성2

    def do_stop(self):  # 기능1(self를 받는게 이 클래스에 포함된 기능임을 말하는 것)
        print('STOP!')

    def do_start(self):  # 기능2
        print('TART!')

    def printcarinfo(self):
        print(f'색상 : {self.color}')
        print(f'색상 : {self.length}')


# 객체 생성 by,생성자 호출
# Car()를 '생성자 호출' 이라 하고, 그 안에 변수를 넣어 color과 length를 선언하는 것을 '속성값 초기화'라고 한다다
Car1 = Car('red',200)
Car2 = Car('blue', 300)

Car1.print_carinfo()
Car2.print_carinfo()
