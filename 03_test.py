# 구구단 함수가 연쇄적으로 호출되도록 함수를 선언해보자
def gugu2():
    for i in range(1,10):
        print('2 * {} = {}'.format(i, i*2))
    gugu3()

def gugu3():
    for i in range(1,10):
        print('3 * {} = {}'.format(i, i*3))
    gugu4()

def gugu4():
    for i in range(1,10):
        print('4 * {} = {}'.format(i, i*4))
    gugu5()

def gugu5():
    for i in range(1,10):
        print('5 * {} = {}'.format(i, i*5))

gugu2()