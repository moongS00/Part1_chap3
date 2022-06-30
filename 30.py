'''
예외가 발생하지 않은 경우에 실행하는 구문 : try~except~else
else가 필수는 아니다.
except없이 try~else만 쓰면 오류가 발생하니 유의하자
'''

nums = []

n=1
while n < 6:
    try:
        num = int(input('숫자를 입력하세요 : '))  # 숫자가 아닌 경우, int 로 형변환 불가능
    except:
        print('예외 발생!')
        continue
    else:
        if num % 2 == 0 :
            nums.append(num)
            n += 1

        else:
            print('입력한 숫자는 홀수 입니다.', end='')
            print('다시 입력하세요')
            continue
