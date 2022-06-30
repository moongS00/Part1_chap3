'''
finally : 예외 발생과 상관 없이 항상 실행
'''

try:
    data = input('숫자 입력 : ')
    int_data = int(data)

except:
    print('예외발생')
    print('숫자 아님')
    int_data = 0

else:
    if int_data % 2 == 0:
        print('짝수 입니다')
    else:
        print('홀수 입니다')

finally:
    print(f'입력값 : {data}')
    
