#함수 실행결과 반환 : return
def cal(n1,n2):
    res = n1 + n2

    return res

a = cal(10,50)
print(a)


#함수는 return을 만나면 실행을 종료한다
def divde(n):
    if n % 2 == 0:
        return '짝수'
    else:
        return '홀수'

    print('Hello')  #출력되지 않음


print(divde(5))