# 사용자로부터 숫자 5개를 입력받을 때 숫자가 아닌 자료형이 입력되면 예외처리하는 프로그램을 만들어보자
nums = []

n=1
while n < 6:
    try:
        num = int(input('숫자를 입력하세요 : '))  # 숫자가 아닌 경우, int 로 형변환 불가능
    except:
        print('예외 발생!')
        continue

    nums.append(num)
    n += 1

print(f'nums : {nums}')