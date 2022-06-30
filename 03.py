#1. 함수 내에서 또다른 함수 호출하기
def fun1():
    print('fun1 호출!')
    fun2()
    print('fun2 호출 후에 실행!') #함수 실행 순서에 유의하기

def fun2():
    print('fun2 호출!')
    fun3()

def fun3():
    print('fun3 호출!')

fun1()


#2. pass를 이용해 실행문 생략 가능
def funto():
    pass

funto()