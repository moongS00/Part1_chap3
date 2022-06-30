#1. 로또 번호(6개)를 출력하는 모듈을 만들어보자
import mymodul

a = mymodul.lottery()

print(f'이번주 행운의 번호는 : {a}')

#2. 문자열을 거꾸로 반환하는 모듈을 만들어보자
user_str = input('문자열 입력 : ')
r_str = mymodul.reverse(user_str)
print(f'거꾸로 출력하기 : {r_str}')