# 예외처리
# 예외란, 문법적인 문제는 없으나 실행 중 발생하는 예상하지 못한 문제
def add(n1, n2):
    print(n1 + n2)


def sub(n1, n2):
    print(n1 - n2)


def mul(n1, n2):
    print(n1 * n2)


def div(n1, n2):
    print(n1 / n2)


n1 = int(input('n1 : '))
n2 = int(input('n2 : '))
add(n1 , n2)
sub(n1 , n2)
mul(n1 , n2)
div(n1 , n2)  # 예외 발생 : 0으로 나눔

# 예외 관련 클래스는 Exception클래스를 상속한다
