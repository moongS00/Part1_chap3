# 인수와 대개변수
def greet(customer):        #customer를 매개변수 라고 한다 (호출부와 선언부를 연결해준다)
    print(f'{customer} 고객님 안녕하세요')

greet('홍길동')  #'홍길동'을 인수 라고 한다


#인수와 매개변수 개수는 일치해야 한다
def addFun(n1, n2):
    print('{} + {} = {}'.format(n1, n2, (n1 + n2)))

addFun(3,5)


#매개변수 개수가 정해지지 않은 경우, *를 이용한다
def printNumber(*numbers):
    for number in numbers:
        print(number, end='')
    print()

printNumber()
printNumber(1)
printNumber(1,2)
printNumber(1,2,3)
printNumber(1,2,3,4)
printNumber(1,2,3,4,5)