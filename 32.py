'''
Exception 클래스 :
    예외를 담당하는 클래스. 파이썬 내부에 존재

except Exception as e:
    print(f'exception : {e}')
'''
n1 = int(input('n1 : '))
n2 = int(input('n2 : '))

try:
    print(f'n1 / n2 : {n1 / n2}')
except Exception as e:
    print(f'exception : {e}')

print(f'n1 * n2 : {n1 * n2}')
print(f'n1 - n2 : {n1 - n2}')
print(f'n1 + n2 : {n1 + n2}')


'''
raise 키워드를 이용하면 예외를 발생시킬 수 있다
'''

def divCal(a1, a2):
    if a2 != 0:
        print(f'{a1} / {a2} = {a1 / a2}')

    else:
        raise Exception('0으로 나눌 수 없습니다.')  # n2가 0이 아닌 경우에 일부러 예외를 발생시킴(예상치 못한 예외가 아님)


a1 = int(input('a1 : '))
a2 = int(input('a2 : '))

try:
    divCal(a1, a2)
except Exception as e:
    print(f'exception : {e}')  # 위에서 Exception을 '0으로 나눌 수 없습니다'로 지정함