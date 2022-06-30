#--------------------------------------전역변수
'''
함수 밖에서 선언된 변수
어디에서나 사용 가능하지만, 함수 안에서 수정할 수 없다@
'''

num1 = 10
def printNumber1():
    print('number : {}'.format(num1))

printNumber1()
print('number : {}'.format(num1))


def printNumber2():
    num1 = 20
    print('number : {} 함수 안에서 수정'.format(num1))

printNumber2()
print('number : {} 하지만 함수 밖에서는 변경되지 않았다'.format(num1))

#----------------------------------------지역변수
'''
함수 안에서 선언된 변수
함수 안에서만 사용 가능하다
'''

def printNumber3():
    num2 = 44
    print('number : {}'.format(num2))

printNumber3()
#print(num2)

#-------------------------------------global 키워드
'''
global을 사용하면 함수 안에서도 전역변수의 값을 수정할 수 있다
'''

def printNumber2():
    global num1
    num1 = 20
    print('number : {} 함수 안에서 수정'.format(num1))

printNumber2()
print('number : {} global 때문에 함수 밖에서도 변경되었다'.format(num1))