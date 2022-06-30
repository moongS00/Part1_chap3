# 사용자로부터 숫자 5개를 입력받아 짝수, 홀수, 실수로 구분해서 각각을 리스트에 저장하는 프로그램을 만들어보자

even_List = []; odd_List = []; float_List = []

n=1

while  n < 6 :

    try:
        num = float(input('숫자를 입력하세요 : '))
    except:
        print('문자입니다. 숫자를 입력하세요.')
        continue
    else:
        if num - int(num) != 0:
            float_List.append(num)

        else:
            if num % 2 == 0:
                even_List.append(int(num))

            else:
                odd_List.append(int(num))

        n += 1

print(f'even_List : {even_List}')
print(f'odd_List  : {odd_List}')
print(f'float_List : {float_List}')