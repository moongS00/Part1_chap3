# 예외처리 : try~except
n1 = 10 ; n2 = 0

try:
    print(n1/n2)
except:
    print('예상치 못한 문제가 발생했습니다.')
    print('다음 프로그램이 정상 실행됩니다.')

print(n1*n2)
print(n1-n2)
print(n1+n2)