#1. 오늘 날씨를 출력하는 함수를 선언하고 3번 호출해보자
def printWeather():
    print('오늘 날씨는 맑습니다. 기온은 25도 입니다.')

printWeather()
printWeather()
printWeather()


#2. 정수 두개를 입력하면 곱셈과 나눗셈 연산 결과를 출력하는 함수를 만들고 호출해보자.
def calFun():
    n1 = int(input('n1 입력: '))
    n2 = int(input('n2 입력: '))

    print(f'n1 * n2 = {n1 * n2}')
    print(f'n1 / n2 = {n1 / n2}')

calFun()
