#1. 길이 cm를 입력하면 mm로 환산한 값을 반환하는 함수를 만들어보자

def cmtomm(cm):
    res = cm * 10

    return res

leng = float(input('길이(cm) 입력 : '))
val = cmtomm(leng)

print(val,'mm')

#2. 1부터 100까지의 정수 중에서 홀수인 난수를 반환하는 함수를 선언하자
import random
def getodd():
    while True:
        rn = random.randint(1,100)
        if rn % 2 != 0:
            break

    return rn

print('홀수 : ',getodd())