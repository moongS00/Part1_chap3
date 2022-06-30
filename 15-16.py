'''
#15
site-packages에 있는 모듈은 어떤 디렉토리에서든지 사용할 수 있다
'''

'''
#16
자주 사용하는 모듈
'''

'''
#1.수학(math)
list_var = [2,5,3.14,58,10,2]
print('-----기본함수-----')
print(f'합 : sum(list_var) : {sum(list_var)}')
print(f'최댓값 : max(list_var) : {max(list_var)}')
print(f'최솟값 : min(list_var) : {min(list_var)}')
print(f'거듭제곱 : pow(13,2) : {pow(13,2)}')
print(f'반올림 : round(3.141592, 3) : {round(3.141592, 3)}')

import math
print('-----math모듈-----')
print(f'절댓값 : math.fabs(-10) : {math.fabs(-10)}')
print(f'절댓값 : math.fabs(-0.125) : {math.fabs(-0.125)}')
print(f'올림 : math.ceil(5.21) : {math.ceil(5.21)}')
print(f'올림 : math.ceil(-5.21) : {math.ceil(-5.21)}')
print(f'내림 : math.floor(5.21) : {math.floor(5.21)}')
print(f'내림 : math.floor(-5.21) : {math.floor(-5.21)}')
print(f'버림 : math.trunc(5.21) : {math.trunc(5.21)}')
print(f'버림 : math.trunc(-5.21) : {math.trunc(-5.21)}')
print(f'최대공약수 : math.gcd(14,21) : {math.gcd(14,21)}')
print(f'팩토리얼 : math.factorial(10) : {math.factorial(10)}')
print(f'제곱근 : math.sqrt(12) : {math.sqrt(12)}')
'''

#2.난수(random)



#3.시간(time)
import time
lt = time.localtime()
print(f'time.localtime() : {lt}')
print(f'lt.tm_year : {lt.tm_year}')
print(f'lt.tm_mon : {lt.tm_mon}')
print(f'lt.tm_mday : {lt.tm_mday}')
print(f'lt.tm_hour : {lt.tm_hour}')
print(f'lt.tm_min : {lt.tm_min}')
print(f'lt.tm_sec : {lt.tm_sec}')
print(f'lt.tm_wday : {lt.tm_wday}') #요일: 0에서 시작