# 사용자 예외 클래스 : 예외 클래스 직접 만들기
# Exception 클래스를 상속해서 사용사 예외 클래스를 만들 수 있음
class NotZero(Exception):
    def __init__(self, n):
        super().__init__(f'{n}은 사용할 수 없습니다!')

def div(num1, num2):
    if num2 == 0:
        raise NotZero(num2)
    else:
        print(f'{num1} / {num2} = {num1/num2}')

num1 = int(input('num1 : '))
num2 = int(input('num2 : '))

try:
    div(num1, num2)
except NotZero as e:
    print(e)